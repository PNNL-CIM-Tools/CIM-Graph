import base64
import enum
import logging
from dataclasses import is_dataclass

import requests

import cimgraph
from cimgraph.data_profile.identity import Identity

_log = logging.getLogger(__name__)


INDENT = '    '

def short_attr_mermaid(obj: object, attr: str, num_indent: int = 1) -> str:
    """
    Generate a mermaid short representation of an attribute.

    Args:
        obj (object): The object containing the attribute.
        attr (str): The attribute name.
        num_indent (int, optional): Number of indentations. Defaults to 1.

    Returns:
        str: The mermaid representation of the attribute.
    """
    mermaid = ''
    edge = getattr(obj, attr)
    if len(attr) > 22:
        mermaid += f'\n{INDENT*(num_indent)}{attr[:22]}\n'
        mermaid += f'{INDENT*(num_indent)}{attr[22:]}:'
    else:
        mermaid += '\n' + INDENT*(num_indent) + f'{attr}: '
    if len(str(edge)) > 22:
        mermaid += f'{edge[:22]}\n'
        mermaid += f'{edge[22:]}'
    else:
        mermaid += f'{edge}'
    return mermaid

def short_uri_mermaid(obj: object, num_indent: int = 1) -> str:
    """
    Generate a mermaid short representation of an object's URI.

    Args:
        obj (object): The object.
        num_indent (int, optional): Number of indentations. Defaults to 1.

    Returns:
        str: The mermaid representation of the object's URI.
    """
    mermaid = ''
    obj_class = obj.__class__.__name__
    short_uri = obj.uri().split('-')[0]
    if len(obj_class) > 22:
        mermaid += INDENT*(num_indent) + short_uri + f'(**{obj_class[:22]}**\n'
        mermaid += INDENT*(num_indent+1) + f'**{obj_class[22:]}**'
    else:
        mermaid += INDENT*(num_indent) + short_uri + f'(**{obj_class}**'
    if 'name' in obj.__dataclass_fields__:
        mermaid += short_attr_mermaid(obj, 'name', num_indent+1)
    else:
        mermaid += INDENT*(num_indent+2) + obj.uri() + '\n'
    mermaid += ')\n'
    return mermaid

def object_mermaid(obj: object) -> str:
    """
    Generate a mermaid mindmap of an object.

    Args:
        obj (object): The object to represent.

    Returns:
        str: The mermaid mindmap representation of the object.
    """
    mermaid = 'mindmap\n'
    # Build starting node as round circle with all attributes that are not None
    mermaid += short_uri_mermaid(obj).replace('(','((')[:-2]
    for attribute in obj.__dataclass_fields__:
        edge = getattr(obj, attribute)
        if type(edge) in [str, bool, float, int] and attribute not in ['name','mRID']:
            mermaid += short_attr_mermaid(obj, attribute, num_indent=2)
    mermaid += '))\n'

    # Expand and build all connected objects
    for attribute in obj.__dataclass_fields__:
        edge = getattr(obj, attribute)
        if is_dataclass(edge) and edge is not None:
            if len(attribute) > 22:
                mermaid += f'\n{INDENT*2}[{attribute[:22]}\n'
                mermaid += f'{INDENT*2}{attribute[22:]}]\n'
            else:
                mermaid += INDENT*2 + f'[{attribute}]\n'
            mermaid += short_uri_mermaid(edge, num_indent=3)

        elif type(edge) == list and edge != []:
            if len(attribute) > 22:
                mermaid += f'\n{INDENT*2}[{attribute[:22]}\n'
                mermaid += f'{INDENT*2}{attribute[22:]}]\n'
            else:
                mermaid += INDENT*2 + f'["{attribute}"]\n'
            for item in edge:
                if is_dataclass(item):
                    mermaid += short_uri_mermaid(item, num_indent=3)

    return mermaid

def class_mermaid(cim_class: type, show_attributes: bool = True, show_inherited: bool = False) -> str:
    """
    Generate a mermaid class diagram of a CIM class.

    Args:
        cim_class (type): The CIM class to represent.
        show_attributes (bool, optional): Whether to show class attributes. Defaults to True.
        show_inherited (bool, optional): Whether to show inherited attributes. Defaults to False.

    Returns:
        str: The mermaid class diagram representation of the CIM class.
    """
    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    mermaid = ''

    if type(cim_class) is not enum.EnumMeta:# and len(parent_classes) > 1:
        mermaid = INDENT + 'class ' + cim_class.__name__ + '{\n'
        if show_attributes:
            for attribute in cim_class.__annotations__.keys():
                attr = cim_class.__dataclass_fields__[attribute]
                attr_type = str(attr.type)
                try:
                    if 'Attribute' in attr.metadata['type']:
                        edge = attr_type.split('[')[1].split(']')[0]
                        mermaid += f'{INDENT*2}+ {attribute}: {edge}\n'
                    elif 'enumeration' in attr.metadata['type']:
                        edge = attr_type.split('[')[1].split(']')[0]
                        mermaid += f'{INDENT*2}+ {attribute}: enum:{edge}\n'
                except:
                    pass

            if show_inherited:
                for parent in parent_classes:
                    if len(parent.__annotations__.keys()) > 0 and parent.__name__ != cim_class.__name__:
                        for attribute in parent.__annotations__.keys():
                            attr = parent.__dataclass_fields__[attribute]
                            attr_type = str(attr.type)
                            try:
                                if 'Attribute' in attr.metadata['type'] or 'enumeration' in attr.metadata['type']:
                                    edge = attr_type.split('[')[1].split(']')[0]
                                    mermaid += f'{INDENT*2}+ {attribute} : {edge}\n'
                            except:
                                pass
        mermaid += INDENT + '}\n'
    elif type(cim_class) is enum.EnumMeta:
        mermaid = INDENT + 'class ' + cim_class.__name__ + ':::enum {\n'
        mermaid += INDENT*2 + '<<enumeration>>\n'
        for value in cim_class.__members__.keys():
            mermaid += INDENT*2 + value + '\n'
        mermaid += '}\n'

    return mermaid

def class_assc_mermaid(cim_class: type, association: str) -> str:
    """
    Generate a mermaid class association diagram.

    Args:
        cim_class (type): The CIM class to represent.
        association (str): The association name.

    Returns:
        str: The mermaid class association diagram.
    """
    attr = cim_class.__dataclass_fields__[association]
    attr_type = str(attr.type)
    mermaid = ''
    try:
        if 'Association' in attr.metadata['type'] or 'Of Aggregate' in attr.metadata['type']:
            edge = attr_type.split('[')[1].split(']')[0].replace('|', 'or')
            if 'list' in attr_type:
                mermaid += f'{INDENT}{cim_class.__name__} --> "0..*" {edge} : {association} \n'
            else:
                mermaid += f'{INDENT}{cim_class.__name__} --> "0..1" {edge} : {association} \n'
        elif 'Aggregate Of' in attr.metadata['type']:
            edge = attr_type.split('[')[1].split(']')[0].replace('|', 'or')
            if 'list' in attr_type:
                mermaid += f'{INDENT}{cim_class.__name__} --o "0..*" {edge} : {association} \n'
            else:
                mermaid += f'{INDENT}{cim_class.__name__} --o "0..1" {edge} : {association} \n'
    except:
        pass
    return mermaid

def class_all_assc_mermaid(cim_class: type, show_inherited: bool = False) -> str:
    """
    Generate a mermaid diagram of all class associations.

    Args:
        cim_class (type): The CIM class to represent.
        show_inherited (bool, optional): Whether to show inherited associations. Defaults to False.

    Returns:
        str: The mermaid diagram of all class associations.
    """
    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    mermaid = ''

    if type(cim_class) is not enum.EnumMeta and len(parent_classes) > 1:
        mermaid += INDENT + f'{parent_classes[1].__name__} <|-- {cim_class.__name__} : inherits from\n'

        for attribute in cim_class.__annotations__.keys():
            mermaid += class_assc_mermaid(cim_class, attribute)

        if show_inherited:
            for parent_class in parent_classes:
                if len(parent_class.__annotations__.keys()) > 0 and parent_class.__name__ != cim_class.__name__:
                    for attribute in parent_class.__annotations__.keys():
                        mermaid += class_assc_mermaid(cim_class, attribute)

    return mermaid

def get_mermaid(root: object | type | list, show_attributes: bool = True, show_inherited: bool = False,
                theme: str = 'neutral', layout: str = 'dagre') -> str:
    """
    Generate a mermaid representation of provided root object or class.

    Args:
        root (object | type | list): The root object or class to represent.
        show_attributes (bool, optional): Whether to show attributes. Defaults to True.
        show_inherited (bool, optional): Whether to show inherited attributes. Defaults to False.
        theme (str, optional): The theme for mermaid diagram. Defaults to 'neutral'.
        layout (str, optional): The layout for mermaid diagram. Defaults to 'dagre'.

    Returns:
        str: The mermaid diagram representation.
    """
    mermaid = ''
    if isinstance(root, Identity) or type(root) is enum.EnumMeta:
        mermaid = object_mermaid(root)
    elif is_dataclass(root):
        mermaid = '%%{init: {"theme":"' + str(theme) + "'}}%%\n"
        mermaid += 'classDiagram\n'
        mermaid += class_mermaid(root, show_attributes, show_inherited)
        mermaid += class_all_assc_mermaid(root, show_inherited)
    elif type(root) == list:
        if set(map(type, root)) == {type} or set(map(type, root)) == {enum.EnumMeta, type}:
            mermaid = '%%{init: {"theme":"' + str(theme) + "'}}%%\n"
            mermaid += 'classDiagram\n'
            for value in root:
                mermaid += class_mermaid(value, show_attributes, show_inherited)
                for attr in value.__annotations__:
                    try:
                        next_str = value.__annotations__[attr]
                        next_class_name = next_str.split('[')[1].split(']')[0]
                        next_class = getattr(value.__module__, next_class_name)
                        if next_class in root:
                            mermaid += class_assc_mermaid(value, attr)
                    except:
                        pass
                parent_classes = list(value.__mro__)
                if len(parent_classes) > 1:
                    if parent_classes[1] in root:
                        mermaid += INDENT + f'{parent_classes[1].__name__} <|-- {value.__name__} : inherits from\n'

        if set(map(isinstance, root, [Identity] * len(root))) == {True}:
            mermaid = ''
            for value in root:
                mermaid += object_mermaid(value)

    return mermaid

def add_object_path_mermaid(root: object, path: str, mermaid: str) -> str:
    """
    Add a path representation to an existing mermaid diagram of an object.

    Args:
        root (object): The root object.
        path (str): The attribute path.
        mermaid (str): The initial mermaid diagram.

    Returns:
        str: The updated mermaid diagram with the path representation.
    """
    edge = root
    previous_edge = root
    if type(path) is list:
        pass
    elif type(path) is str:
        path = path.split('.')

    for attr in path:
        if isinstance(edge, Identity):
            if '[' in attr:
                attr_list = attr.split('[')
                next_edge = getattr(edge, attr_list[0])
                next_edge = eval(f'next_edge[{attr_list[1]}')
            else:
                next_edge = getattr(edge, attr)
        elif type(edge) is list:
            next_edge = eval(f'edge{attr}')
            edge = previous_edge
            attr = previous_attr

        if isinstance(next_edge, Identity):
            # Add an arrow to next class
            short_uri = edge.uri().split('-')[0]
            next_short_uri = next_edge.uri().split('-')[0]
            mermaid += INDENT + f'{short_uri} -- "{attr}" --> {next_short_uri}\n'
            text = short_uri_mermaid(next_edge)
            mermaid += text.replace('(', '("').replace(')', '")')

        elif type(next_edge) in [str, float, bool, int]:
            mermaid = mermaid[:-3]
            mermaid += short_attr_mermaid(edge, attr, num_indent=2)
            mermaid += '")\n'
        previous_attr = attr
        previous_edge = edge
        edge = next_edge
    return mermaid

def add_class_path_mermaid(root: type, path: str | list[str], mermaid: str,
                           show_attributes: bool = True, show_inherited: bool = False) -> str:
    """
    Add a class path representation to an existing mermaid diagram.

    Args:
        root (type): The root class.
        path (str | list[str]): The attribute path.
        mermaid (str): The initial mermaid diagram.
        show_attributes (bool, optional): Whether to show attributes. Defaults to True.
        show_inherited (bool, optional): Whether to show inherited attributes. Defaults to False.

    Returns:
        str: The updated mermaid diagram with the class path representation.
    """
    edge = root
    if type(path) is list:
        pass
    elif type(path) is str:
        path = path.split('.')
    for attr in path:
        if '__subclasses__' in attr:
            next_class = eval(f'edge.{attr}')
            mermaid += INDENT + f'{edge.__name__} <|-- {next_class.__name__} : inherits from\n'
        else:
            mermaid += class_assc_mermaid(edge, attr)
            next_str = edge.__dataclass_fields__[attr]
            next_class_name = next_str.type.split('[')[1].split(']')[0]
            next_class = getattr(edge.__module__, next_class_name)
            mermaid += class_mermaid(next_class, show_attributes, show_inherited)
        edge = next_class
    return mermaid

def get_mermaid_path(root: object | type, path: str | list[str],
                     direction: str = 'LR', theme: str = 'neutral',
                     show_attributes: bool = True, show_inherited: bool = False) -> str:
    """
    Generate a mermaid diagram of a specified path starting from a root object or class.
    The path is a cimgraph traversal (e.g. '.Terminals[0].ConnectivityNode') or
    a list with UML association names separated by commas (e.g. ['Terminals','[0]'])

    Args:
        root (object | type): The root object or class.
        path (str, list[str]): The attribute path
        direction (str, optional): The direction of the diagram. Defaults to 'LR'.
        theme (str, optional): The theme for the diagram. Defaults to 'neutral'.
        show_attributes (bool, optional): Whether to show attributes. Defaults to True.
        show_inherited (bool, optional): Whether to show inherited attributes. Defaults to False.

    Returns:
        str: The mermaid diagram representation of the specified path.
    """
    mermaid = ''
    if isinstance(root, Identity):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += f'flowchart {direction}\n'
        mermaid += short_uri_mermaid(root).replace('(', '("').replace(')', '")')
        mermaid = add_object_path_mermaid(root, path, mermaid)
    elif isinstance(root, enum.EnumMeta):
        mermaid = ''
    elif is_dataclass(root):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += 'classDiagram\n'
        mermaid += class_mermaid(root, show_inherited)
        mermaid = add_class_path_mermaid(root, path, mermaid, show_attributes, show_inherited)
    return mermaid

def add_mermaid_path(root: object | type, path: str | list[str], mermaid: str,
                     show_attributes: bool = True, show_inherited: bool = False) -> str:
    """
    Add a mermaid path representation to an existing diagram.

    Args:
        root (object | type): The root object or class.
        path (str, list[str]): The attribute path.
        mermaid (str): The initial mermaid diagram.
        show_attributes (bool, optional): Whether to show attributes. Defaults to True.
        show_inherited (bool, optional): Whether to show inherited attributes. Defaults to False.

    Returns:
        str: The updated mermaid diagram with the path representation.
    """
    if isinstance(root, Identity):
        mermaid += short_uri_mermaid(root).replace('(', '("').replace(')', '")')
        mermaid = add_object_path_mermaid(root, path, mermaid)
    elif isinstance(root, enum.EnumMeta):
        mermaid = ''
    elif is_dataclass(root):
        mermaid = add_class_path_mermaid(root, path, mermaid, show_attributes, show_inherited)
    return mermaid

def download_mermaid(mermaid:str, filename:str) -> None:
    """
    Downloads a Mermaid diagram from mermaid.ink and saves as an image

    Args:
        mermaid (str): The mermaid diagram text.
        filename (str): The file to which the diagram should be saved

    Returns:
        None
    """
    try:
        graphbytes = mermaid.encode('ascii')
        base64_bytes = base64.b64encode(graphbytes)
        base64_string = base64_bytes.decode('ascii')

        url='https://mermaid.ink/img/' + base64_string


        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    except requests.exceptions.RequestException as e:
        _log.error(f'Error downloading diagram')
