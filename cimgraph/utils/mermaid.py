import enum
from dataclasses import is_dataclass

import cimgraph
from cimgraph.data_profile.identity import Identity

INDENT = '    '

def short_attr_mermaid(obj:object, attr:str, num_indent:int=1) -> str:
    mermaid = ''
    edge = getattr(obj, attr)
    if len(attr) > 20:
        mermaid += f'\n{INDENT*(num_indent)}{attr[:20]}\n'
        mermaid += f'{INDENT*(num_indent)}{attr[20:]}:'
    else:
        mermaid += '\n' + INDENT*(num_indent) + f'{attr}: '
    if len(str(edge)) > 20:
        mermaid += f'{edge[:20]}\n'
        mermaid += f'{edge[20:]}'
    else:
        mermaid += f'{edge}'
    return mermaid


def short_uri_mermaid(obj:object, num_indent:int=1) -> str:
    mermaid = ''
    obj_class = obj.__class__.__name__
    short_uri = obj.uri().split('-')[0]
    if len(obj_class) > 20:
        mermaid += INDENT*(num_indent) + short_uri + f'(**{obj_class[:20]}**\n'
        mermaid += INDENT*(num_indent+1) + f'**{obj_class[20:]}**'
    else:
        mermaid += INDENT*(num_indent) + short_uri + f'(**{obj_class}**'
    if 'name' in obj.__dataclass_fields__:
        mermaid += short_attr_mermaid(obj, 'name', num_indent+1)
    else:
        mermaid += INDENT*(num_indent+2) + obj.uri() + '\n'
    mermaid += ')\n'
    return mermaid




def object_mermaid(obj:object) -> str:

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
            if len(attribute) > 20:
                mermaid += f'\n{INDENT*2}[{attribute[:20]}\n'
                mermaid += f'{INDENT*2}{attribute[20:]}]\n'
            else:
                mermaid += INDENT*2 + f'[{attribute}]\n'
            mermaid += short_uri_mermaid(edge, num_indent=3)

        elif type(edge) == list and edge != []:
            if len(attribute) > 20:
                mermaid += f'\n{INDENT*2}[{attribute[:20]}\n'
                mermaid += f'{INDENT*2}{attribute[20:]}]\n'
            else:
                mermaid += INDENT*2 + f'["{attribute}"]\n'
            for item in edge:
                if is_dataclass(item):
                    mermaid += short_uri_mermaid(item, num_indent=3)

    return mermaid

def class_mermaid(cim_class:type, show_attributes:bool=True, show_inherited:bool=False)->str:

    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    if type(cim_class) is not enum.EnumMeta and len(parent_classes)>1:
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
    return mermaid

def class_assc_mermaid(cim_class:type, association:str)->str:
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

def class_all_assc_mermaid(cim_class:type, show_inherited:bool=False)->str:

    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    if type(cim_class) is not enum.EnumMeta and len(parent_classes)>1:
        mermaid = INDENT + f'{parent_classes[1].__name__} <|-- {cim_class.__name__} : inherits from\n'

        for attribute in cim_class.__annotations__.keys():
            mermaid += class_assc_mermaid(cim_class, attribute)

        if show_inherited:

            for parent_class in parent_classes:
                if len(parent_class.__annotations__.keys()) > 0 and parent_class.__name__ != cim_class.__name__:

                    for attribute in parent_class.__annotations__.keys():
                        mermaid += class_assc_mermaid(cim_class, attribute)

    return mermaid

def get_mermaid(root:object|type|list, show_attributes:bool=True,
                show_inherited:bool=False, theme:str='dark'):
    if isinstance(root, Identity):
        mermaid = object_mermaid(root)
    elif isinstance(root, enum.EnumMeta):
        mermaid = ''
    elif is_dataclass(root):
        mermaid = "%%{init: {'theme':'" + str(theme) + "'}}%%\n"
        mermaid += 'classDiagram\n'
        mermaid += class_mermaid(root, show_attributes, show_inherited)
        mermaid += class_all_assc_mermaid(root, show_inherited)
    elif type(root) == list:

            if set(map(type, root)) == {type}:
                mermaid = "%%{init: {'theme':'" + str(theme) + "'}}%%\n"
                mermaid += 'classDiagram\n'
                for value in root:
                    mermaid += class_mermaid(value, show_attributes, show_inherited)
                    for attr in value.__annotations__:
                        try:
                            next_str = value.__annotations__[attr]
                            next_class_name=next_str.split('[')[1].split(']')[0]
                            next_class = eval(f'{value.__module__}.{next_class_name}')
                            if next_class in root:
                                mermaid += class_assc_mermaid(value, attr)
                        except:
                            pass
                    parent_classes = list(value.__mro__)
                    if len(parent_classes)>1:
                        if parent_classes[1] in root:
                            mermaid += INDENT + f'{parent_classes[1].__name__} <|-- {value.__name__} : inherits from\n'


            if set(map(isinstance, root, [Identity]*len(root))) == {True}:
                mermaid = ''
                for value in root:
                    mermaid += object_mermaid(value)

    return mermaid

def add_object_path_mermaid(root:object, path:list[str], mermaid:str)->str:
    edge = root
    previous_edge = root
    for attr in path:
        if isinstance(edge, Identity):
            next_edge = getattr(edge,attr)
        elif type(edge) is list:
            next_edge = eval(f'edge{attr}')
            edge = previous_edge
            attr = previous_attr

        if isinstance(next_edge, Identity):
            # Add an arrow to next class
            short_uri = edge.uri().split('-')[0]
            next_short_uri = next_edge.uri().split('-')[0]
            mermaid += INDENT + f'{short_uri} -- {attr} --> {next_short_uri}\n'
            text = short_uri_mermaid(next_edge)
            mermaid += text.replace('(','("').replace(')','")')

        elif type(next_edge) in [str, float, bool, int]:
            mermaid = mermaid[:-3]
            mermaid += short_attr_mermaid(edge, attr, num_indent=2)
            mermaid += '")\n'
        previous_attr = attr
        previous_edge = edge
        edge = next_edge
    return mermaid

def add_class_path_mermaid(root:type, path:list[str], mermaid:str,
                           show_attributes:bool=True, show_inherited:bool=False)->str:
    edge = root
    for attr in path:
        if '__subclasses__' in attr:
            next_class = eval(f'edge.{attr}')
            mermaid += INDENT + f'{edge.__name__} <|-- {next_class.__name__} : inherits from\n'
        else:
            mermaid += class_assc_mermaid(edge, attr)
            next_str = edge.__dataclass_fields__[attr]
            next_class_name=next_str.type.split('[')[1].split(']')[0]
            next_class = eval(f'{edge.__module__}.{next_class_name}')
            mermaid += class_mermaid(next_class, show_attributes, show_inherited)
        edge = next_class
    return mermaid

def get_mermaid_path(root:object|type, path:list[str],
                     direction:str='LR', theme:str='neutral',
                     show_attributes:bool=True, show_inherited:bool=False)->str:

    if isinstance(root, Identity):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += f'flowchart {direction}\n'
        mermaid += short_uri_mermaid(root).replace('(','("').replace(')','")')
        mermaid = add_object_path_mermaid(root, path, mermaid)
    elif isinstance(root, enum.EnumMeta):
        mermaid = ''
    elif is_dataclass(root):
        mermaid = '%%{init: {"theme":"' + str(theme) + '"}}%%\n'
        mermaid += 'classDiagram\n'
        mermaid += class_mermaid(root, show_inherited)
        mermaid = add_class_path_mermaid(root, path, mermaid, show_attributes, show_inherited)
    return mermaid

def add_mermaid_path(root:object|type, path:list[str],mermaid:str)->str:

    if isinstance(root, Identity):
        mermaid += short_uri_mermaid(root).replace('(','("').replace(')','")')
        mermaid = add_object_path_mermaid(root, path, mermaid)
    elif isinstance(root, enum.EnumMeta):
        mermaid = ''
    elif is_dataclass(root):
        pass
    return mermaid
