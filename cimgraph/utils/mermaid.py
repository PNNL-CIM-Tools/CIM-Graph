import enum
from dataclasses import is_dataclass

from cimgraph.data_profile.identity import Identity


def object_mermaid(self):

    mermaid = 'mindmap\n'
    indent = '    '
    mermaid += indent+f'''root((**{self.__class__.__name__}**'''
    for attribute in self.__dataclass_fields__:
        edge = getattr(self, attribute)
        if type(edge) in [str, bool, float] and attribute != 'mRID':
            if len(attribute) > 20:
                mermaid += f'\n{indent*2}{attribute[:20]}\n'
                mermaid += f'{indent*2}{attribute[20:]}:'
            else:
                mermaid += '\n' + indent*2 + f'{attribute}: '
            if len(str(edge)) > 20:
                mermaid += f'{edge[:20]}\n'
                mermaid += f'{edge[20:]}'
            else:
                mermaid += f'{edge}'

    mermaid += '))\n'

    for attribute in self.__dataclass_fields__:
        edge = getattr(self, attribute)
        if is_dataclass(edge) and edge is not None:
            if len(attribute) > 20:
                mermaid += f'\n{indent*2}[{attribute[:20]}\n'
                mermaid += f'{indent*2}{attribute[20:]}]\n'
            else:
                mermaid += indent*2 + f'[{attribute}]\n'
            edge_class = edge.__class__.__name__
            if len(edge_class) > 20:
                mermaid += indent*3 + f'(**{edge_class[:20]}**\n'
                mermaid += indent*3 + f'**{edge_class[20:]}**'
            else:
                mermaid += indent*3 + f'(**{edge_class}**'
            if 'name' in edge.__dataclass_fields__:
                if len(edge.name) > 20:
                    mermaid += f'\n{indent*4}{edge.name[:20]}\n'
                    mermaid += f'{indent*4}{edge.name[20:]})\n'
                else:
                    mermaid += f'\n{indent*4}{edge.name})\n'
            else:
                mermaid += indent*4 + edge.uri() + '\n'
        elif type(edge) == list and edge != []:
            if len(attribute) > 20:
                mermaid += f'\n{indent*2}[{attribute[:20]}\n'
                mermaid += f'{indent*2}{attribute[20:]}]\n'
            else:
                mermaid += indent*2 + f'["{attribute}"]\n'
            for item in edge:
                if is_dataclass(item):
                    item_class = item.__class__.__name__
                    if len(item_class) > 20:
                        mermaid += indent*3 + f'(**{item_class[:20]}**\n'
                        mermaid += indent*3 + f'**{item_class[20:]}**'
                    else:
                        mermaid += indent*3 + f'(**{item_class}**'
                    if 'name' in item.__dataclass_fields__:
                        if len(item.name) > 20:
                            mermaid += f'\n{indent*4}{item.name[:20]}\n'
                            mermaid += f'{indent*4}{item.name[20:]})\n'
                        else:
                            mermaid += f'\n{indent*4}{item.name})\n'
                    else:
                        mermaid += indent*4 + item.uri() + '\n'

    return mermaid

def class_mermaid(cim_class:type, show_inherited:bool=False, theme:str='dark'):
    indent = '    '
    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    if type(cim_class) is not enum.EnumMeta and len(parent_classes)>1:
        mermaid = "%%{init: {'theme':'" + str(theme) + "'}}%%\n"
        mermaid += 'classDiagram\n'
        mermaid += indent + 'class ' + cim_class.__name__ + '{\n'

        for attribute in cim_class.__annotations__.keys():
            attr = cim_class.__dataclass_fields__[attribute]
            attr_type = str(attr.type)
            try:
                if 'Attribute' in attr.metadata['type'] or 'Enumeration' in attr.metadata['type']:
                    edge = attr_type.split('[')[1].split(']')[0]

                    mermaid += f'{indent*2}+ {attribute} : {edge}\n'
            except:
                pass

        if show_inherited:

            for parent in parent_classes:
                if len(parent.__annotations__.keys()) > 0 and parent.__name__ != cim_class.__name__:

                    for attribute in parent.__annotations__.keys():
                        attr = parent.__dataclass_fields__[attribute]
                        attr_type = str(attr.type)
                        try:
                            if 'Attribute' in attr.metadata['type'] or 'Enumeration' in attr.metadata['type']:
                                edge = attr_type.split('[')[1].split(']')[0]

                                mermaid += f'{indent*2}+ {attribute} : {edge}\n'
                        except:
                            pass

        mermaid += indent + '}\n'

        mermaid += indent + f'{parent_classes[1].__name__} <|-- {cim_class.__name__} : inherits from\n'

        for attribute in cim_class.__annotations__.keys():
            attr = cim_class.__dataclass_fields__[attribute]
            attr_type = str(attr.type)
            try:
                if 'Association' in attr.metadata['type'] or 'Of Aggregate' in attr.metadata['type']:
                    edge = attr_type.split('[')[1].split(']')[0].replace('|', 'or')
                    if 'list' in attr_type:
                        mermaid += f'{indent}{cim_class.__name__} --> "many" {edge} : {attribute} \n'
                    else:
                        mermaid += f'{indent}{cim_class.__name__} --> "one" {edge} : {attribute} \n'
                elif 'Aggregate Of' in attr.metadata['type']:
                    edge = attr_type.split('[')[1].split(']')[0].replace('|', 'or')
                    if 'list' in attr_type:
                        mermaid += f'{indent}{cim_class.__name__} --o "many" {edge} : {attribute} \n'
                    else:
                        mermaid += f'{indent}{cim_class.__name__} --o "one" {edge} : {attribute} \n'
            except:
                pass

        if show_inherited:

            for parent in parent_classes:
                if len(parent.__annotations__.keys()) > 0 and parent.__name__ != cim_class.__name__:

                    for attribute in parent.__annotations__.keys():
                        attr = parent.__dataclass_fields__[attribute]
                        attr_type = str(attr.type)

                        try:
                            if 'Association' in attr.metadata['type'] or 'Of Aggregate' in attr.metadata['type']:
                                edge = attr_type.split('[')[1].split(']')[0].replace('|', 'or')
                                if 'list' in attr_type:
                                    mermaid += f'{indent}{cim_class.__name__} --> "many" {edge} : {attribute} \n'
                                else:
                                    mermaid += f'{indent}{cim_class.__name__} --> "one" {edge} : {attribute} \n'
                            elif 'Aggregate Of' in attr.metadata['type']:
                                edge = attr_type.split('[')[1].split(']')[0].replace('|', 'or')
                                if 'list' in attr_type:
                                    mermaid += f'{indent}{cim_class.__name__} --o "many" {edge} : {attribute} \n'
                                else:
                                    mermaid += f'{indent}{cim_class.__name__} --o "one" {edge} : {attribute} \n'
                        except:
                            pass
    return mermaid

def get_mermaid(root:object|type, show_inherited:bool=False, theme:str='dark'):
    if isinstance(root, Identity):
        mermaid = object_mermaid(root)
    elif isinstance(root, enum.EnumMeta):
        mermaid = ''
    elif is_dataclass(root):
        mermaid = class_mermaid(root, show_inherited, theme)

    return mermaid
