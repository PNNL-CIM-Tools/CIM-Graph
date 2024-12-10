import json
import logging
from dataclasses import dataclass, field, is_dataclass
from typing import Optional
from uuid import UUID

from cimgraph.utils import UUID_Meta
from cimgraph.utils.timing import timing as time_func

ARCHIVE_JSON_LD = True

_log = logging.getLogger(__name__)

@dataclass
class Identity():
    '''
    This is the new root class from CIM 18 to provide common identification
    for all classes needing identification and naming attributes.
    IdentifiedObject is now a child class of Identity.
    mRID is superseded by Identity.identifier, which is typed to be a UUID.
    '''
    identifier: Optional[UUID] = field(
        default = None,
        metadata = {
            'type': 'Attribute',
            'minOccurs': '1',
            'maxOccurs': '1'
        })

    # Backwards support for objects created with mRID
    @time_func
    def __post_init__(self) -> None:
        # Validate if pre-specified
        if self.identifier is not None:
            id = str(self.identifier)
            # Check if Identity.identifier is an invalid UUID
            if not isinstance(self.identifier,UUID):
                _log.warning(f'Identifier {self.identifier} must be a UUID object, generating new UUID')
                self.identifier = None
            # If object inherits from IdentifiedObject, create uuid from mRID
            if 'mRID' in self.__dataclass_fields__:
                self.uuid(uri=id, mRID=self.mRID, name=self.name)
            else:
                self.uuid(uri=id)
        # Otherwise, create a new UUID
        else:
            if 'mRID' in self.__dataclass_fields__:
                self.uuid(mRID=self.mRID, name=self.name)
            else:
                self.uuid()

        if ARCHIVE_JSON_LD:
            self.__json_ld__ = json.dumps({'@id': f'{str(self.identifier)}', '@type': f'{self.__class__.__name__}'})

    # Override python string for printing with JSON representation
    @time_func
    def __str__(self, print_mRID:bool = False) -> str:
        # Create JSON-LD dump with repr and all attributes
        dump = dict(json.loads(self.__repr__()) | self.__dict__)
        del dump['__uuid__']
        del dump['__json_ld__']
        attribute_list = list(self.__dataclass_fields__.keys())
        for attribute in attribute_list:
            # Delete attributes from print that are empty
            if dump[attribute] is None or dump[attribute] == []:
                del dump[attribute]
            # If a dataclass, replace with custom repr
            elif is_dataclass(dump[attribute]):
                dump[attribute] = dump[attribute].__repr__()
            elif type[dump[attribute]] != str:
                # Reformat all attributes as string for JSON
                dump[attribute] = str(dump[attribute])
        if not print_mRID:
            del dump['identifier']
            if 'mRID' in dump:
                del dump['mRID']
        # Fix python ' vs JSON "
        dump = json.dumps(dump)
        dump = str(dump).replace('\\\"','\"' )
        dump = str(dump).replace('\"[','[' )
        dump = str(dump).replace(']\"',']' )
        dump = str(dump).replace('\"{','{' )
        dump = str(dump).replace('}\"','}' )
        return dump

    # Override python __repr__ method with JSON-LD representation
    # This is needed to avoid infinite loops in object previews
    @time_func
    def __repr__(self) -> str:
        if ARCHIVE_JSON_LD:
            return self.__json_ld__
        else:
            return json.dumps({'@id': f'{str(self.identifier)}', '@type': f'{self.__class__.__name__}'})

    # Add indentation of json for pretty print
    def pprint(self, print_mRID:bool=False) -> None:
        print(json.dumps(json.loads(self.__str__(print_mRID)), indent=4))

    # Create UUID from inconsistent mRIDs
    @time_func
    def uuid(self, mRID:str = None, uri:str = None, name:str = None, seed:str = None) -> UUID:
        self.__uuid__ = UUID_Meta()
        if seed is None:
            seed = ''
        if name is not None:
            seed = seed + f'{self.__class__.__name__}:{name}'

        self.identifier = self.__uuid__.generate_uuid(mRID=mRID, uri=uri, name=name, seed=seed)

        # Write mRID string for backwards compatibility
        if 'mRID' in self.__dataclass_fields__:
            if mRID is not None:
                self.mRID = mRID
            else:
                self.mRID = str(self.identifier)


    # Method to reconstitute URI from UUID
    def uri(self) -> str:
        uri = str(self.identifier)
        try:
            if self.__uuid__.uri_is_capitalized:
                uri = uri.upper()
            if self.__uuid__.uri_has_underscore:
                uri = '_' + uri
        except:
            pass
        return uri
