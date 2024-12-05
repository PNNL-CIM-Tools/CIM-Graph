from __future__ import annotations

import json
import logging
from random import Random
from uuid import UUID, uuid4

_log = logging.getLogger(__name__)

class UUID_Meta():
    uuid:UUID = None
    uri_has_underscore:bool = False
    uri_is_capitalized:bool = False
    mrid_has_underscore:bool = False
    mrid_is_capitalized:bool = False


    # Create UUID from inconsistent mRIDs
    def generate_uuid(self, mRID:str = None, uri:str = None, name:str = None, seed:str = None) -> UUID:
        if seed is None:
            seed = ''
        invalid_mrid = True

        # If URI is specified, try creating from UUID from URI
        if uri is not None:
            # Handle inconsistent capitalization / underscores
            if uri.strip('_') != uri:
                self.uri_has_underscore = True
            if uri.lower() != uri:
                self.uri_is_capitalized = True
            try:
                self.uuid = UUID(uri.strip('_').lower())
                identifier = self.uuid
                invalid_mrid = False
            except:
                seed = seed + uri
                _log.warning(f'URI {uri} not a valid UUID, generating new UUID')
                mRID = str(uri)
            else:
                self.uuid = identifier
                invalid_mrid = False

        # If URI is specified, try creating from UUID from URI
        if mRID is not None:
            # Handle inconsistent capitalization / underscores
            if mRID.strip('_') != mRID:
                self.mrid_has_underscore = True
                if uri is None:
                    self.uri_has_underscore = True
            if mRID.lower() != mRID:
                self.mrid_is_capitalized = True
                if uri is None:
                    self.uri_is_capitalized = True
            # Create a new UUID based on the mRID if it does not exist
            if self.uuid is None:
                try:
                    identifier = UUID(mRID.strip('_').lower())
                    invalid_mrid = False
                except:
                    seed = seed + mRID
                    _log.warning(f'mRID {mRID} not a valid UUID, generating new UUID')

        # Otherwise, build UUID using unique name as a seed
        if invalid_mrid:

            if seed:
                randomGenerator = Random(seed)
                self.uuid = UUID(int=randomGenerator.getrandbits(128), version=4)
            else:
                self.uuid = uuid4()

            identifier = self.uuid

        return identifier
