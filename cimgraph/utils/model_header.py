from __future__ import annotations

from datetime import datetime, timezone
from uuid import NAMESPACE_URL, uuid4, uuid5

from cimgraph.core import get_model_authority, get_model_name


def model_header() -> dict:
    """
    Returns the values for the md:FullModel and cim:ModelAuthority header written
    at the top of exported files.

    The FullModel UUID is new for every export (it identifies one file/version).
    The ModelAuthority UUID is derived from the authority name so it is stable.
    """
    authority = get_model_authority()
    return {
        'full_model_uuid': str(uuid4()),
        'created': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'model_name': get_model_name(),
        'authority': authority,
        'authority_uuid': str(uuid5(NAMESPACE_URL, authority)),
    }
