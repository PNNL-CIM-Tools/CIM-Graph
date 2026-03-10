"""
Runtime CIM profile merging.

Combines multiple CIM sub-profile modules (e.g. connectivity, electrical)
into a single synthetic module with merged dataclasses.

Overlapping classes get the union of their fields.  Non-overlapping classes
are adopted as-is but reparented onto the merged inheritance chain.

Usage::

    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    conn = BlazegraphConnection(cim_override=merged)
"""
from __future__ import annotations

import dataclasses
import logging
import types
from collections import defaultdict
from dataclasses import dataclass, field, is_dataclass
from enum import Enum

from cimgraph.data_profile.identity import Identity
from cimgraph.data_profile.units import CIMUnit

_log = logging.getLogger(__name__)

# ── helpers ────────────────────────────────────────────────────────────

_PROPERTY_NAMES = frozenset({
    '__namespace__', '__package__', '__minOccurs__', '__maxOccurs__',
})


def _get_direct_fields(cls):
    """Return only the fields declared directly on *cls*, not inherited ones."""
    inherited: set[str] = set()
    for base in cls.__mro__[1:]:
        if hasattr(base, '__dataclass_fields__'):
            inherited.update(base.__dataclass_fields__)
    return {
        name: f
        for name, f in cls.__dataclass_fields__.items()
        if name not in inherited
    }


def _clone_field(f: dataclasses.Field):
    """Recreate a ``dataclasses.field()`` descriptor from an existing Field."""
    kwargs: dict = {
        'metadata': f.metadata,
        'repr': f.repr,
        'compare': f.compare,
        'init': f.init,
    }
    if f.default is not dataclasses.MISSING:
        kwargs['default'] = f.default
    elif f.default_factory is not dataclasses.MISSING:
        kwargs['default_factory'] = f.default_factory
    return field(**kwargs)


def _collect_properties(cls):
    """Gather ``@property`` descriptors that live on *cls* itself (not bases)."""
    props: dict[str, property] = {}
    for name in _PROPERTY_NAMES:
        # Walk MRO manually so we only grab the definition from this class
        if name in cls.__dict__ and isinstance(cls.__dict__[name], property):
            props[name] = cls.__dict__[name]
    return props


def _classify(obj):
    """Return 'dataclass', 'enum', 'cimunit', or 'other'."""
    if is_dataclass(obj) and isinstance(obj, type):
        return 'dataclass'
    if isinstance(obj, type) and issubclass(obj, Enum):
        return 'enum'
    if isinstance(obj, type) and issubclass(obj, CIMUnit):
        return 'cimunit'
    return 'other'


def _is_profile_dataclass(cls):
    """True for dataclasses that descend from Identity (profile classes)."""
    return is_dataclass(cls) and isinstance(cls, type) and issubclass(cls, Identity)


# ── topological sort ───────────────────────────────────────────────────

def _topo_sort(names: list[str], class_defs: dict[str, list[type]]) -> list[str]:
    """
    Return *names* in topological order (parents before children).

    Uses the MRO of each class to find dependencies.  Only names that
    appear in *class_defs* are considered edges.
    """
    # Build adjacency: name -> set of parent names that are also in class_defs
    deps: dict[str, set[str]] = defaultdict(set)
    all_names = set(names)
    for name in names:
        for cls in class_defs[name]:
            for base in cls.__mro__[1:]:
                bname = base.__name__
                if bname in all_names and bname != name:
                    deps[name].add(bname)

    # Kahn's algorithm
    in_degree = {n: len(deps[n]) for n in names}
    queue = [n for n in names if in_degree[n] == 0]
    result: list[str] = []
    while queue:
        queue.sort()          # deterministic ordering
        node = queue.pop(0)
        result.append(node)
        for n in names:
            if node in deps[n]:
                deps[n].discard(node)
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)

    if len(result) != len(names):
        missing = set(names) - set(result)
        raise RuntimeError(
            f'Cyclic dependency detected among: {missing}'
        )
    return result


# ── class creation ─────────────────────────────────────────────────────

def _resolve_base(cls, merged_module):
    """
    Find the first real parent of *cls* (i.e. the direct base that isn't
    ``object``) and return the merged version if it exists, otherwise
    return the original.
    """
    for base in cls.__mro__[1:]:
        if base is object:
            continue
        bname = base.__name__
        if hasattr(merged_module, bname):
            return getattr(merged_module, bname)
        return base
    return object


def _build_class(name: str, definitions: list[type],
                 merged_module: types.ModuleType) -> type:
    """
    Create a single merged dataclass from one or more *definitions* of the
    same class name.
    """
    # ── 1. Determine the base class ────────────────────────────────────
    merged_base = _resolve_base(definitions[0], merged_module)

    # ── 2. Collect the union of direct fields ──────────────────────────
    all_fields: dict[str, tuple[str, dataclasses.Field]] = {}
    for cls in definitions:
        for fname, f in _get_direct_fields(cls).items():
            if fname not in all_fields:
                all_fields[fname] = (f.type, f)

    # ── 3. Collect @property descriptors ───────────────────────────────
    props: dict[str, property] = {}
    for cls in definitions:
        props.update(_collect_properties(cls))

    # ── 4. Build the class namespace ───────────────────────────────────
    namespace: dict = {}
    annotations: dict[str, str] = {}

    # Separate fields with defaults from those without, because dataclasses
    # require non-default fields to come before default fields.
    fields_no_default: list[tuple[str, str, dataclasses.Field]] = []
    fields_with_default: list[tuple[str, str, dataclasses.Field]] = []

    for fname, (ftype, f) in all_fields.items():
        has_default = (
            f.default is not dataclasses.MISSING
            or f.default_factory is not dataclasses.MISSING
        )
        if has_default:
            fields_with_default.append((fname, ftype, f))
        else:
            fields_no_default.append((fname, ftype, f))

    for fname, ftype, f in fields_no_default + fields_with_default:
        annotations[fname] = ftype
        namespace[fname] = _clone_field(f)

    # Attach properties
    for pname, prop in props.items():
        namespace[pname] = prop

    namespace['__annotations__'] = annotations

    # ── 5. Create the class ────────────────────────────────────────────
    new_cls = type(name, (merged_base,), namespace)
    new_cls = dataclass(repr=False)(new_cls)

    # ── 6. Carry over __stereotype__ ───────────────────────────────────
    for cls in definitions:
        if hasattr(cls, '__stereotype__'):
            new_cls.__stereotype__ = cls.__stereotype__
            break

    # Copy the docstring from the first definition
    for cls in definitions:
        if cls.__doc__:
            new_cls.__doc__ = cls.__doc__
            break

    return new_cls


# ── main entry point ───────────────────────────────────────────────────

def merge_profiles(*modules: types.ModuleType) -> types.ModuleType:
    """
    Merge multiple CIM profile modules into a single synthetic module.

    Args:
        *modules: Two or more imported profile modules, for example
            ``cimgraph.data_profile.cim18gmdm.connectivity`` and
            ``cimgraph.data_profile.cim18gmdm.electrical``.

    Returns:
        A ``types.ModuleType`` instance that behaves like a regular
        profile module: it has an ``__all__`` list and every class is
        accessible via ``getattr(merged, class_name)``.

    Example::

        from cimgraph.data_profile.cim18gmdm import connectivity, electrical
        merged = merge_profiles(connectivity, electrical)
    """
    if len(modules) < 2:
        raise ValueError('merge_profiles requires at least two modules')

    # ── 1. Collect all exported names and their classes ────────────────
    class_defs: dict[str, list[type]] = defaultdict(list)
    class_category: dict[str, str] = {}

    for mod in modules:
        mod_all = getattr(mod, '__all__', [])
        for name in mod_all:
            obj = getattr(mod, name, None)
            if obj is None:
                continue
            if not isinstance(obj, type):
                continue
            class_defs[name].append(obj)
            cat = _classify(obj)
            # Keep the most specific category if it differs
            if name not in class_category:
                class_category[name] = cat

    all_names = list(class_defs.keys())

    # ── 2. Topological sort ────────────────────────────────────────────
    sorted_names = _topo_sort(all_names, class_defs)

    # ── 3. Build the merged module ─────────────────────────────────────
    merged = types.ModuleType('merged_cim_profile')
    merged.__all__ = []

    # Pre-populate with Identity so _resolve_base can find it
    setattr(merged, 'Identity', Identity)

    for name in sorted_names:
        definitions = class_defs[name]
        cat = class_category[name]

        if name == 'Identity':
            # Always use the real Identity class — it has uri(), uuid(),
            # __post_init__(), etc. that must not be lost in a rebuild.
            merged_cls = Identity
        elif cat in ('enum', 'cimunit', 'other'):
            # For non-dataclass types, take the first definition
            merged_cls = definitions[0]
        elif cat == 'dataclass':
            if _is_profile_dataclass(definitions[0]):
                merged_cls = _build_class(name, definitions, merged)
            else:
                # Non-Identity dataclass (unusual but handle it)
                merged_cls = definitions[0]
        else:
            merged_cls = definitions[0]

        setattr(merged, name, merged_cls)
        merged.__all__.append(name)

    _log.info(
        'Merged %d classes from %d profile modules',
        len(merged.__all__), len(modules),
    )
    return merged
