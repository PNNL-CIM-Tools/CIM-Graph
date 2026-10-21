from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from cimprofiles.identity import model_authority_namespace

from cimgraph.core import get_model_authority, get_model_name


def model_header() -> dict:
    """
    Returns the values for the md:FullModel and cim:ModelAuthority header written
    at the top of exported files.

    The FullModel UUID is new for every export (it identifies one file/version).
    The ModelAuthority UUID is derived from the authority URI, so it is stable, and it
    is the namespace of every UUID the authority seeds from names and non-UUID mRIDs.
    """
    authority = get_model_authority()
    return {
        'full_model_uuid': str(uuid4()),
        'created': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'model_name': get_model_name(),
        'authority': authority,
        'authority_uuid': str(model_authority_namespace(authority)),
    }
