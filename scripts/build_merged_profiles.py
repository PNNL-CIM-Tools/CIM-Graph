"""Build pre-baked merged profile __init__.py files from merge_releases.yaml.

Run from the repo root:
    python scripts/build_merged_profiles.py

Each entry in merge_releases.yaml produces a committed __init__.py that
re-exports the merged class surface. The file is a normal Python module —
Pylance reads it directly, and `import cimgraph.data_profile.<name> as cim`
resolves to the merged class set with no runtime merge machinery needed.

For classes that appear in only one sub-profile, the output is a simple
re-import. For classes that overlap across sub-profiles (same name, different
fields in each), the output is an inline @dataclass definition that carries the
union of all direct fields — this is the case for CGMES where e.g. ACLineSegment
appears in both EQ (r, x, bch) and SC (r0, x0, b0ch) sub-profiles.

Add this to the PyPI release process for any profile listed in the config.
"""
from __future__ import annotations

import dataclasses
import importlib
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).parent.parent
_CONFIG = _REPO_ROOT / 'cimgraph' / 'data_profile' / 'merge_releases.yaml'

# Ensure the repo is importable when run directly.
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


def _load_config() -> list[dict]:
    with open(_CONFIG) as f:
        data = yaml.safe_load(f)
    return data['releases']


def _sanitize_metadata(meta: dict) -> dict:
    """Strip newlines from string metadata values so repr() is safe in source."""
    return {
        k: v.replace('\n', ' ').strip() if isinstance(v, str) else v
        for k, v in meta.items()
    }


def _field_source(f: dataclasses.Field) -> str:
    """Emit a field(...) expression that recreates the field descriptor."""
    parts: list[str] = []
    if f.default is not dataclasses.MISSING:
        parts.append(f'default={f.default!r}')
    elif f.default_factory is not dataclasses.MISSING:
        factory = f.default_factory
        if factory is list:
            parts.append('default_factory=list')
        elif factory is dict:
            parts.append('default_factory=dict')
        else:
            parts.append(f'default_factory={factory.__name__}')
    meta = _sanitize_metadata(dict(f.metadata))
    parts.append(f'metadata={meta!r}')
    return f'field({", ".join(parts)})'


def _emit_inline_class(name: str, merged_cls: type, merged_base_name: str) -> list[str]:
    """Emit an inline @dataclass definition for an overlapping class."""
    from cimgraph.data_profile.merge import _get_direct_fields
    direct = _get_direct_fields(merged_cls)
    lines: list[str] = []
    lines.append('@dataclass(repr=False)')
    lines.append(f'class {name}({merged_base_name}):')

    # Preserve the original docstring — make_dataclass overwrites __doc__ with
    # the signature string, so we must emit it explicitly.
    doc = merged_cls.__doc__
    if doc and not doc.startswith(f'{name}('):
        # Indent each line of the docstring body by 4 spaces.
        indented = '\n'.join('    ' + l for l in doc.split('\n'))
        lines.append(f'    """{indented.strip()}\n    """')

    if not direct:
        lines.append('    pass')
    else:
        for fname, f in direct.items():
            ftype = f.type if isinstance(f.type, str) else str(f.type)
            field_expr = _field_source(f)
            # Never wrap — the metadata repr contains string literals that
            # textwrap would break mid-literal, producing a SyntaxError.
            lines.append(f'    {fname}: {ftype} = {field_expr}')
    return lines


def _build_init(release: dict) -> str:
    """Return the generated __init__.py content for one release entry."""
    from cimgraph.data_profile.identity import Identity
    from cimgraph.data_profile.merge import _get_direct_fields, merge_profiles

    parts = release['parts']
    description = release.get('description', '')
    package = release['package']

    modules = [importlib.import_module(p) for p in parts]
    merged = merge_profiles(*modules)

    names = sorted(merged.__all__)

    # ── Determine which classes are overlapping vs single-source ──────────
    # A class is "overlapping" if the same name with *different field sets*
    # appears in more than one sub-profile.  For those we emit an inline
    # @dataclass.  For single-source (or Identity/enum/cimunit), we re-import.
    name_to_parts: dict[str, list[str]] = defaultdict(list)
    name_to_first_part: dict[str, str] = {}
    for part_path, mod in zip(parts, modules):
        for n in getattr(mod, '__all__', []):
            if n not in name_to_first_part:
                name_to_first_part[n] = part_path
            name_to_parts[n].append(part_path)

    # Collect the merged module's class objects
    merged_classes: dict[str, type] = {}
    for n in names:
        obj = getattr(merged, n, None)
        if obj is not None and isinstance(obj, type):
            merged_classes[n] = obj

    # An overlapping dataclass is one where the merged object is NOT the same
    # object as in the first-seen sub-profile (merge_profiles rebuilt it).
    from cimgraph.data_profile.merge import _is_profile_dataclass
    overlapping: set[str] = set()
    for n, cls in merged_classes.items():
        if not _is_profile_dataclass(cls) or n == 'Identity':
            continue
        first_mod = importlib.import_module(name_to_first_part[n])
        first_cls = getattr(first_mod, n, None)
        if first_cls is not None and cls is not first_cls:
            overlapping.add(n)

    # ── Topological order for the inline dataclass section ─────────────────
    # Only overlapping dataclasses need topo sorting (parents before children).
    from cimgraph.data_profile.merge import _topo_sort
    class_defs_for_sort: dict[str, list[type]] = {
        n: [merged_classes[n]] for n in overlapping if n in merged_classes
    }
    topo_overlapping = _topo_sort(list(overlapping), class_defs_for_sort)

    # ── Imports for non-overlapping names ──────────────────────────────────
    part_to_simple: dict[str, list[str]] = defaultdict(list)
    for n in sorted(names):
        if n not in overlapping:
            src = name_to_first_part.get(n, parts[0])
            part_to_simple[src].append(n)

    import_lines: list[str] = []
    for part_path in parts:
        part_names = part_to_simple.get(part_path, [])
        if not part_names:
            continue
        header = f'from {part_path} import ('
        joined = ', '.join(part_names)
        wrapped_names = textwrap.fill(
            joined,
            width=88,
            initial_indent='    ',
            subsequent_indent='    ',
            break_long_words=False,
            break_on_hyphens=False,
        )
        import_lines.append(f'{header}\n{wrapped_names})')

    # ── Inline @dataclass section ──────────────────────────────────────────
    # We need 'dataclass' and 'field' in scope for the generated code.
    inline_lines: list[str] = []
    for n in topo_overlapping:
        cls = merged_classes[n]
        # Base: the first real base in the merged class's MRO
        base = cls.__bases__[0]
        base_name = base.__name__
        inline_lines.append('')
        inline_lines.extend(_emit_inline_class(n, cls, base_name))

    # ── __all__ ────────────────────────────────────────────────────────────
    all_entries = '\n'.join(f"    '{n}'," for n in names)
    parts_comment = '\n'.join(f'#   {p}' for p in parts)

    has_inline = bool(inline_lines)
    # Inline @dataclass fields use 'Optional[...]' and 'UUID' in their type
    # annotations.  Without these imports Pylance resolves them as Any.
    inline_imports = (
        'from dataclasses import dataclass, field\n'
        'from typing import Optional\n'
        'from uuid import UUID\n'
        if has_inline else ''
    )

    return f'''\
"""Merged profile: {package}

{description}

Parts:
{parts_comment}

Generated by scripts/build_merged_profiles.py — do not edit by hand.
Re-run the script after adding or updating sub-profile parts.
"""
from __future__ import annotations

{inline_imports}{chr(10).join(import_lines)}
{''.join(line + chr(10) for line in inline_lines)}
__all__ = [
{all_entries}
]
'''


def main() -> None:
    releases = _load_config()
    for release in releases:
        package = release['package']

        print(f'Building {package} ...')
        content = _build_init(release)

        # Write to the package __init__.py.
        package_dir = _REPO_ROOT / Path(*package.split('.'))
        if not package_dir.is_dir():
            raise FileNotFoundError(
                f'Package directory not found: {package_dir}\n'
                f'Create it and add sub-profile packages before running this script.'
            )

        init_path = package_dir / '__init__.py'
        init_path.write_text(content, encoding='utf-8')
        print(f'  wrote {init_path.relative_to(_REPO_ROOT)}')

        # Smoke-test: the written file must be importable and expose __all__.
        if package in sys.modules:
            del sys.modules[package]
        mod = importlib.import_module(package)
        assert hasattr(mod, '__all__'), f'{package}.__all__ missing after write'
        print(f'  ok — {len(mod.__all__)} classes exported')


if __name__ == '__main__':
    main()
