import base64
import enum
import logging
from dataclasses import Field, fields, is_dataclass

import requests

import cimgraph
from cimgraph.data_profile.identity import Identity
from cimgraph.data_profile.units import CIMUnit

_log = logging.getLogger(__name__)


INDENT = '    '
WRAP = 22


def _wrap(text: str) -> list[str]:
    """Split a string into WRAP-length chunks (1 chunk if short)."""
    if len(text) <= WRAP:
        return [text]
    return [text[:WRAP], text[WRAP:]]


def _inner_type(attr_type: str) -> str:
    """Extract inner type name from a typing string like 'Optional[Foo]' or 'list[Foo]'.

    Returns empty string if no brackets found.
    """
    if '[' not in attr_type or ']' not in attr_type:
        return ''
    return attr_type.split('[', 1)[1].rsplit(']', 1)[0]


def _stereotypes(field_obj: Field) -> list[str]:
    """Return the UML stereotypes for a dataclass field.

    Supports both the new XSL output (separate 'stereotypes' list metadata key)
    and older profiles where stereotypes leaked into the 'type' key
    (e.g. 'OfAggregate', 'enumeration Attribute').
    """
    meta = field_obj.metadata
    if 'stereotypes' in meta:
        return list(meta['stereotypes'])
    # Legacy fallback: split the 'type' string on whitespace and drop known roles
    raw = meta.get('type', '')
    return [tok for tok in raw.split() if tok not in ('Attribute', 'Association')]


def _role(field_obj: Field) -> str:
    """Return the structural role: 'Attribute' or 'Association'.

    Normalizes legacy profiles where the role was polluted with stereotype labels.
    """
    raw = field_obj.metadata.get('type', '')
    if 'Attribute' in raw or 'enumeration' in raw:
        return 'Attribute'
    # Legacy stereotypes that replaced 'Association'
    legacy_assoc = ('OfAggregate', 'Of Aggregate', 'AggregateOf', 'Aggregate Of',
                    'Association', 'informative', 'IRC-DR', 'harmonization')
    if any(s in raw for s in legacy_assoc):
        return 'Association'
    return raw or 'Attribute'


def _is_enum_field(field_obj: Field) -> bool:
    raw = field_obj.metadata.get('type', '')
    return 'enumeration' in raw or 'enumeration' in _stereotypes(field_obj)


def _is_aggregate_of(field_obj: Field) -> bool:
    """Reverse aggregation end — rendered with filled-diamond arrow (--o)."""
    raw = field_obj.metadata.get('type', '')
    if 'AggregateOf' in raw or 'Aggregate Of' in raw:
        return True
    return any('AggregateOf' in s or 'Aggregate Of' in s for s in _stereotypes(field_obj))


def _is_list(field_obj: Field) -> bool:
    return field_obj.type.startswith('list')


def _format_value(edge: object) -> str:
    """String form of an attribute value, rounding CIMUnit magnitudes to fit the diagram.

    CIMUnit stores full float precision (e.g. 30.479999999999997 meter); round to
    4 decimals and strip trailing zeros so labels stay compact.
    """
    if isinstance(edge, CIMUnit):
        magnitude = round(float(edge), 4)
        number = f'{magnitude:g}'
        unit = str(edge).split(' ', 1)[1] if ' ' in str(edge) else ''
        return f'{number} {unit}'.rstrip()
    return str(edge)


def short_attr_mermaid(obj: object, attr: str, num_indent: int = 1) -> str:
    """Mermaid short representation of an attribute value."""
    edge = getattr(obj, attr)
    lines = _wrap(attr)
    if len(lines) == 1:
        prefix = '\n' + INDENT * num_indent + f'{attr}: '
    else:
        prefix = f'\n{INDENT*num_indent}{lines[0]}\n{INDENT*num_indent}{lines[1]}:'
    value_lines = _wrap(_format_value(edge))
    return prefix + '\n'.join(value_lines) if len(value_lines) > 1 else prefix + value_lines[0]


def short_uri_mermaid(obj: object, num_indent: int = 1) -> str:
    """Neutral node label for an object: `uri(**Class**\\n  name: ...)`.

    The delimiters are a single `(`/`)` and the label carries no markdown-string
    backticks. Diagram-specific callers wrap this: mindmaps use `((`/`))` (bold
    renders without backticks), flowcharts use ``("` ``/`` `")`` (backticks needed
    for bold). Keep the formatting decisions in those callers, not here.
    """
    obj_class = obj.__class__.__name__
    short_uri = obj.uri().split('-')[0]
    cls_lines = _wrap(obj_class)
    if len(cls_lines) == 1:
        mermaid = INDENT * num_indent + short_uri + f'(**{obj_class}**'
    else:
        mermaid = INDENT * num_indent + short_uri + f'(**{cls_lines[0]}**\n'
        mermaid += INDENT * (num_indent + 1) + f'**{cls_lines[1]}**'
    if 'name' in obj.__dataclass_fields__:
        mermaid += short_attr_mermaid(obj, 'name', num_indent + 1)
    else:
        mermaid += INDENT * (num_indent + 2) + obj.uri() + '\n'
    mermaid += ')\n'
    return mermaid


def _flowchart_node(obj: object, num_indent: int = 1) -> str:
    """Wrap short_uri_mermaid as a flowchart node: ``uri("`**Class**...`")``.

    Flowcharts need markdown-string backticks for the ``**bold**`` to render, so
    the neutral ``(``/``)`` delimiters become ``("` `` / `` `")``.
    """
    return short_uri_mermaid(obj, num_indent).replace('(', '("`', 1).replace(')\n', '`")\n')


def _bracket_label(attribute: str, bracket: str = '[', close: str = ']') -> str:
    """Render an attribute label wrapped to two lines if long, inside the given brackets."""
    lines = _wrap(attribute)
    if len(lines) == 1:
        return INDENT * 2 + f'{bracket}{attribute}{close}\n'
    return f'\n{INDENT*2}{bracket}{lines[0]}\n{INDENT*2}{lines[1]}{close}\n'


def object_mermaid(obj: object) -> str:
    """Mermaid mindmap of an object."""
    mermaid = 'mindmap\n'
    # Mindmap nodes use '((' / '))' and no backticks. short_uri_mermaid ends with
    # ')\n'; strip those 2 chars so scalar/CIMUnit attributes below sit inside the
    # node before we re-close it with '))'.
    mermaid += short_uri_mermaid(obj).replace('(', '((')[:-2]
    for attribute in obj.__dataclass_fields__:
        edge = getattr(obj, attribute)
        is_scalar = type(edge) in (str, bool, float, int) and attribute not in ('name', 'mRID')
        if is_scalar or isinstance(edge, CIMUnit):
            mermaid += short_attr_mermaid(obj, attribute, num_indent=2)
    mermaid += '))\n'

    for attribute in obj.__dataclass_fields__:
        edge = getattr(obj, attribute)
        if isinstance(edge, CIMUnit):
            continue  # already rendered inside the core node above
        if is_dataclass(edge) and edge is not None:
            mermaid += _bracket_label(attribute)
            mermaid += short_uri_mermaid(edge, num_indent=3).replace('(', '((').replace(')', '))')
        elif isinstance(edge, list) and edge:
            mermaid += _bracket_label(attribute, bracket='["', close='"]')
            for item in edge:
                if is_dataclass(item):
                    mermaid += short_uri_mermaid(item, num_indent=3).replace('(', '((').replace(')', '))')
    return mermaid


def _class_header(cim_class: type) -> str:
    """Emit `class Foo{`.

    The UML stereotype annotation (`<<Concrete>>`, `<<informative>>`, etc.) is
    intentionally omitted: the profile labels are noisy and frequently inaccurate
    (e.g. `<<informative>>` on normative classes), so they add clutter without
    conveying reliable information in the rendered diagrams.
    """
    mermaid = INDENT + 'class ' + cim_class.__name__ + '{\n'
    # Stereotype emission disabled — see docstring.
    # stereotype = cim_class.__dict__.get('__stereotype__')
    # if stereotype is not None:
    #     try:
    #         mermaid += INDENT * 2 + f'<<{stereotype.value}>>\n'
    #     except AttributeError:
    #         pass
    return mermaid


def _iter_fields(cim_class: type, include_inherited: bool):
    """Yield (attribute_name, Field) pairs for the class, optionally including parent fields."""
    for attribute in cim_class.__annotations__:
        yield attribute, cim_class.__dataclass_fields__[attribute]
    if include_inherited:
        parents = list(cim_class.__mro__)[1:-1]
        for parent in parents:
            if not hasattr(parent, '__annotations__'):
                continue
            for attribute in parent.__annotations__:
                if attribute in cim_class.__annotations__:
                    continue
                if attribute in parent.__dataclass_fields__:
                    yield attribute, parent.__dataclass_fields__[attribute]


def _field_visible(field_obj: Field, serialize_only: bool) -> bool:
    if not serialize_only:
        return True
    return field_obj.metadata.get('serialize', True)


def class_mermaid(cim_class: type, show_attributes: bool = True, show_inherited: bool = False,
                  serialize_only: bool = False) -> str:
    """Mermaid class diagram of a CIM class."""
    if issubclass(cim_class, CIMUnit):
        instance = cim_class(0)
        mermaid = _class_header(cim_class)
        mermaid += INDENT * 2 + 'value: float \n'
        mermaid += INDENT * 2 + 'unit: ' + getattr(instance, 'unit').value + ' \n'
        mermaid += INDENT * 2 + 'multiplier: ' + getattr(instance, 'multiplier').value + ' \n'
        mermaid += INDENT + '}\n'
        return mermaid

    if isinstance(cim_class, enum.EnumMeta):
        mermaid = INDENT + 'class ' + cim_class.__name__ + ':::enum {\n'
        for value in cim_class.__members__:
            mermaid += INDENT * 2 + value + '\n'
        mermaid += '}\n'
        return mermaid

    mermaid = _class_header(cim_class)
    if show_attributes:
        for attribute, field_obj in _iter_fields(cim_class, include_inherited=show_inherited):
            if _role(field_obj) != 'Attribute':
                continue
            if not _field_visible(field_obj, serialize_only):
                continue
            edge = _inner_type(str(field_obj.type))
            if not edge:
                continue
            if _is_enum_field(field_obj):
                mermaid += f'{INDENT*2}+ {attribute}: enum:{edge}\n'
            else:
                mermaid += f'{INDENT*2}+ {attribute}: {edge}\n'
    mermaid += INDENT + '}\n'
    return mermaid


def class_assc_mermaid(cim_class: type, association: str, serialize_only: bool = False) -> str:
    """Single mermaid line for one association on a class."""
    field_obj = cim_class.__dataclass_fields__[association]
    if _role(field_obj) != 'Association':
        return ''
    if not _field_visible(field_obj, serialize_only):
        return ''
    edge = _inner_type(str(field_obj.type)).replace('|', 'or')
    if not edge:
        return ''
    cardinality = '"0..*"' if _is_list(field_obj) else '"0..1"'
    arrow = '--o' if _is_aggregate_of(field_obj) else '-->'
    return f'{INDENT}{cim_class.__name__} {arrow} {cardinality} {edge} : {association} \n'


def class_all_assc_mermaid(cim_class: type, show_inherited: bool = False,
                           serialize_only: bool = False) -> str:
    """Mermaid diagram of all class associations (plus inheritance edge)."""
    if isinstance(cim_class, enum.EnumMeta) or issubclass(cim_class, CIMUnit):
        return ''
    parents = list(cim_class.__mro__)[1:-1]
    if not parents:
        return ''

    mermaid = INDENT + f'{parents[0].__name__} <|-- {cim_class.__name__} : inherits from\n'
    for attribute, _ in _iter_fields(cim_class, include_inherited=show_inherited):
        mermaid += class_assc_mermaid(cim_class, attribute, serialize_only=serialize_only)
    return mermaid


def get_mermaid(root: object | type | list, show_attributes: bool = True, show_inherited: bool = False,
                theme: str = 'neutral', layout: str = 'dagre', serialize_only: bool = False) -> str:
    """Generate a mermaid representation of provided root object or class.

    Args:
        root: object, class, or list of classes/objects to represent.
        show_attributes: Whether to show class attributes.
        show_inherited: Whether to show inherited attributes and associations.
        theme: Mermaid theme name.
        layout: Mermaid layout engine name.
        serialize_only: If True, hide fields with metadata 'serialize': False
            (reverse/inverse associations that are not present in the XML serialization).
            Defaults to False so reverse ends are shown.
    """
    if isinstance(root, Identity):
        return object_mermaid(root)

    if is_dataclass(root) or isinstance(root, enum.EnumMeta):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += 'classDiagram\n'
        mermaid += class_mermaid(root, show_attributes, show_inherited, serialize_only=serialize_only)
        mermaid += class_all_assc_mermaid(root, show_inherited, serialize_only=serialize_only)
        return mermaid

    if isinstance(root, list):
        types_in_root = set(map(type, root))
        if types_in_root <= {type, enum.EnumMeta}:
            mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
            mermaid += 'classDiagram\n'
            for value in root:
                mermaid += class_mermaid(value, show_attributes, show_inherited,
                                         serialize_only=serialize_only)
                for attr in value.__annotations__:
                    try:
                        next_class_name = _inner_type(value.__annotations__[attr])
                        next_class = eval(f'{value.__module__}.{next_class_name}')
                        if next_class in root:
                            mermaid += class_assc_mermaid(value, attr, serialize_only=serialize_only)
                    except Exception:
                        pass
                parents = list(value.__mro__)
                if len(parents) > 1 and parents[1] in root:
                    mermaid += INDENT + f'{parents[1].__name__} <|-- {value.__name__} : inherits from\n'
            return mermaid

        if all(isinstance(v, Identity) for v in root):
            return ''.join(object_mermaid(v) for v in root)

    return ''


def add_object_path_mermaid(root: object, path: str, mermaid: str) -> str:
    """Add a path representation to an existing mermaid diagram of an object."""
    edge = root
    previous_edge = root
    previous_attr = None
    if isinstance(path, str):
        path = path.split('.')

    for attr in path:
        if isinstance(edge, Identity):
            if '[' in attr:
                attr_list = attr.split('[')
                attr_value = getattr(edge, attr_list[0])
                next_edge = eval(f'attr_value[{attr_list[1]}')
            else:
                next_edge = getattr(edge, attr)
        elif isinstance(edge, list):
            next_edge = eval(f'edge{attr}')
            edge = previous_edge
            attr = previous_attr

        if isinstance(next_edge, Identity):
            short_uri = edge.uri().split('-')[0]
            next_short_uri = next_edge.uri().split('-')[0]
            mermaid += INDENT + f'{short_uri} -- "{attr}" --> {next_short_uri}\n'
            mermaid += _flowchart_node(next_edge)
        elif isinstance(next_edge, (str, float, bool, int, enum.Enum)):
            mermaid = mermaid[:-4]  # strip trailing '`")\n' to append inside the node
            mermaid += short_attr_mermaid(edge, attr, num_indent=2)
            mermaid += '`")\n'
        previous_attr = attr
        previous_edge = edge
        edge = next_edge
    return mermaid


def add_class_path_mermaid(root: type, path: str | list[str], mermaid: str,
                           show_attributes: bool = True, show_inherited: bool = False,
                           serialize_only: bool = False) -> str:
    """Add a class path representation to an existing mermaid diagram."""
    edge = root
    if isinstance(path, str):
        path = path.split('.')
    for attr in path:
        if '__subclasses__' in attr:
            next_class = eval(f'edge.{attr}')
            mermaid += INDENT + f'{edge.__name__} <|-- {next_class.__name__} : inherits from\n'
        else:
            mermaid += class_assc_mermaid(edge, attr, serialize_only=serialize_only)
            next_class_name = _inner_type(edge.__dataclass_fields__[attr].type)
            next_class = eval(f'{edge.__module__}.{next_class_name}')
        mermaid += class_mermaid(next_class, show_attributes, show_inherited,
                                 serialize_only=serialize_only)
        edge = next_class
    return mermaid


def get_mermaid_path(root: object | type, path: str | list[str],
                     direction: str = 'LR', theme: str = 'neutral',
                     show_attributes: bool = True, show_inherited: bool = False,
                     serialize_only: bool = False) -> str:
    """Generate a mermaid diagram of a specified path starting from a root object or class."""
    if isinstance(root, Identity):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += f'flowchart {direction}\n'
        mermaid += _flowchart_node(root)
        return add_object_path_mermaid(root, path, mermaid)
    if isinstance(root, enum.EnumMeta):
        return ''
    if is_dataclass(root):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += 'classDiagram\n'
        mermaid += class_mermaid(root, show_attributes, show_inherited, serialize_only=serialize_only)
        return add_class_path_mermaid(root, path, mermaid, show_attributes, show_inherited,
                                      serialize_only=serialize_only)
    return ''


def add_mermaid_path(root: object | type, path: str | list[str], mermaid: str,
                     show_attributes: bool = True, show_inherited: bool = False,
                     serialize_only: bool = False) -> str:
    """Add a mermaid path representation to an existing diagram."""
    if isinstance(root, Identity):
        mermaid += _flowchart_node(root)
        return add_object_path_mermaid(root, path, mermaid)
    if isinstance(root, enum.EnumMeta):
        return ''
    if is_dataclass(root):
        return add_class_path_mermaid(root, path, mermaid, show_attributes, show_inherited,
                                      serialize_only=serialize_only)
    return mermaid


def download_mermaid(mermaid: str, filename: str, timeout: int = 30) -> bool:
    """Download a Mermaid diagram from mermaid.ink and save as an image."""
    try:
        graphbytes = mermaid.encode('ascii')
        base64_string = base64.b64encode(graphbytes).decode('ascii')
        url = 'https://mermaid.ink/img/' + base64_string

        with requests.get(url, stream=True, timeout=timeout) as response:
            response.raise_for_status()
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=16384):
                    if chunk:
                        file.write(chunk)
        return True

    except requests.exceptions.Timeout:
        _log.error(f'Timeout error downloading diagram to {filename}')
        return False
    except requests.exceptions.HTTPError as e:
        _log.error(f'HTTP Error {e.response.status_code} downloading diagram to {filename}')
        return False
    except requests.exceptions.ConnectionError:
        _log.error(f'Connection error downloading diagram to {filename}')
        return False
    except requests.exceptions.RequestException as e:
        _log.error(f'Error downloading diagram to {filename}: {str(e)}')
        return False
    except Exception as e:
        _log.error(f'Unexpected error downloading diagram to {filename}: {str(e)}')
        return None
