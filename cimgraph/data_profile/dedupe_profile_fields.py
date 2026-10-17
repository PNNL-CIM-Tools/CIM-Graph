"""Remove duplicate field definitions from generated CIM profile modules.

The cimantic-graphs XSLT emits a class's own associations (serialize=True) and
then the inverse ends that point at it (serialize=False). When a profile
selects both ends of an association, the same field is written twice. Python
keeps the last definition, so serialize=False silently wins.

Each duplicate is classified and logged:

- exporter duplicate: every definition has the same type and inverse (one
  association emitted twice). Fixed in the XSLT; safe to dedupe.
- UML conflict: definitions differ in type or inverse, meaning two distinct
  associations share a role name on this class (e.g. RatioTapChanger has
  RatioTapChanger.TransformerEnd and AdditionalRatioTapChanger.TransformerEnd).
  This needs fixing in the UML model.

In both cases the serialize=True definition is kept (the last one if several),
otherwise the last definition, which is what Python already used at runtime.

Run from the repo root:
    python cimgraph/data_profile/dedupe_profile_fields.py
    python cimgraph/data_profile/dedupe_profile_fields.py --check   # report only
"""
from __future__ import annotations

import argparse
import ast
import logging
import sys
from pathlib import Path

_log = logging.getLogger('dedupe_profile_fields')

PROFILE_ROOT = Path(__file__).parent


def _field_info(node: ast.AnnAssign) -> dict:
    """Extract the annotation and literal metadata entries of a field definition."""
    metadata = {}
    if isinstance(node.value, ast.Call):
        for keyword in node.value.keywords:
            if keyword.arg == 'metadata' and isinstance(keyword.value, ast.Dict):
                for key, value in zip(keyword.value.keys, keyword.value.values):
                    if isinstance(key, ast.Constant) and isinstance(value, ast.Constant):
                        metadata[key.value] = value.value
    return {
        'annotation': ast.unparse(node.annotation),
        'inverse': metadata.get('inverse'),
        'serialize': metadata.get('serialize'),
        'lineno': node.lineno,
    }


def _definition_span(body: list, index: int) -> tuple[int, int]:
    """Return the (first, last) source lines of a field and its docstring."""
    node = body[index]
    end = node.end_lineno
    if index + 1 < len(body):
        following = body[index + 1]
        if (isinstance(following, ast.Expr) and isinstance(following.value, ast.Constant)
                and isinstance(following.value.value, str)):
            end = following.end_lineno
    return node.lineno, end


def find_duplicates(source: str) -> list[dict]:
    """Return one entry per duplicated (class, field), with the definition to keep."""
    duplicates = []
    for class_node in ast.walk(ast.parse(source)):
        if not isinstance(class_node, ast.ClassDef):
            continue
        definitions = {}
        for index, node in enumerate(class_node.body):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                info = _field_info(node)
                info['span'] = _definition_span(class_node.body, index)
                definitions.setdefault(node.target.id, []).append(info)

        for field_name, infos in definitions.items():
            if len(infos) < 2:
                continue
            same_association = len({(info['annotation'], info['inverse']) for info in infos}) == 1
            serialized = [info for info in infos if info['serialize'] is True]
            keep = serialized[-1] if serialized else infos[-1]
            duplicates.append({
                'class': class_node.name,
                'field': field_name,
                'kind': 'exporter duplicate' if same_association else 'UML conflict',
                'keep': keep,
                'drop': [info for info in infos if info is not keep],
                'definitions': infos,
            })
    return duplicates


def remove_definitions(source: str, duplicates: list[dict]) -> str:
    """Delete the dropped definitions (and one trailing blank line each)."""
    lines = source.split('\n')
    spans = sorted((info['span'] for dup in duplicates for info in dup['drop']), reverse=True)
    for first, last in spans:
        if last < len(lines) and lines[last].strip() == '':
            last += 1
        del lines[first - 1:last]
    return '\n'.join(lines)


def _describe(info: dict) -> str:
    return (f"line {info['lineno']}: {info['annotation']}, inverse={info['inverse']}, "
            f"serialize={info['serialize']}")


def log_duplicates(path: Path, duplicates: list[dict]) -> None:
    for dup in duplicates:
        log = _log.warning if dup['kind'] == 'UML conflict' else _log.info
        log(f"{dup['kind']}: {path.relative_to(PROFILE_ROOT)} {dup['class']}.{dup['field']}")
        for info in dup['definitions']:
            marker = 'keep' if info is dup['keep'] else 'drop'
            log(f'    {marker} {_describe(info)}')


def main() -> int:
    parser = argparse.ArgumentParser(description='Remove duplicate field definitions from CIM profiles.')
    parser.add_argument('--check', action='store_true', help='Report duplicates without editing files.')
    parser.add_argument('--log', default='dedupe_profile_fields.log', help='Log file path.')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s',
                        handlers=[logging.FileHandler(args.log, mode='w'), logging.StreamHandler()])

    totals = {'exporter duplicate': 0, 'UML conflict': 0}
    for path in sorted(PROFILE_ROOT.rglob('*.py')):
        source = path.read_text(encoding='utf-8')
        duplicates = find_duplicates(source)
        if not duplicates:
            continue
        log_duplicates(path, duplicates)
        for dup in duplicates:
            totals[dup['kind']] += 1
        if not args.check:
            path.write_text(remove_definitions(source, duplicates), encoding='utf-8')

    _log.info(f"Summary: {totals['exporter duplicate']} exporter duplicates, "
              f"{totals['UML conflict']} UML conflicts")
    if args.check:
        return 1 if any(totals.values()) else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
