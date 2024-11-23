from __future__ import annotations

import json
import logging
from random import Random
from uuid import UUID, uuid4

_log = logging.getLogger(__name__)

def str_to_uuid(obj, uri:str = None, mRID:str = None, name:str = None) -> UUID:
    seed = ''
    invalid = True
    obj.__uuid__ = obj.__uuid_meta__()
    # If uri is specified, try creating from UUID from mRID
    if uri is not None:
        if uri.strip('_') != uri:
            obj.__uuid__.uri_has_underscore = True
        if uri.lower() != uri:
            obj.__uuid__.uri_is_capitalized = True
        try:
            obj.__uuid__.uuid = UUID(uri.strip('_').lower())
            invalid = False
        except:
            seed = seed + uri
            _log.warning(f'Warning: URI {uri} not a valid UUID, generating new UUID')

    if mRID is not None:
        if mRID.strip('_') != mRID:
            obj.__uuid__.mrid_has_underscore = True
        if mRID.lower() != mRID:
            obj.__uuid__.mrid_is_capitalized = True
        if obj.__uuid__.uuid is None:
            try:
                obj.__uuid__.uuid = UUID(mRID.strip('_').lower())
                invalid = False
            except:
                obj.mRID = mRID
                seed = seed + mRID
                _log.warning(f'Warning: mRID {mRID} not a valid UUID, generating new UUID')

    if invalid:
        if name is not None:
            seed = seed + f"{obj.__class__.__name__}:{name}"
            randomGenerator = Random(seed)
            obj.__uuid__.uuid = UUID(int=randomGenerator.getrandbits(128), version=4)
            obj.name = name
        else:
            obj.__uuid__.uuid = uuid4()

    obj.identifier = obj.__uuid__.uuid



    if 'mRID' in obj.__dataclass_fields__:
        if mRID is not None:
            obj.mRID = mRID
        else:
            obj.mRID = str(obj.identifier)

def uri(self):
    uri = str(self.identifier)
    try:
        if self.__uuid__.uri_is_capitalized:
            uri = uri.upper()
        if self.__uuid__.uri_has_underscore:
            uri = '_'+uri
    except:
        pass
    return uri

class __uuid_meta__():
    uuid:UUID = None
    uri_has_underscore:bool = False
    uri_is_capitalized:bool = False
    mrid_has_underscore:bool = False
    mrid_is_capitalized:bool = False
