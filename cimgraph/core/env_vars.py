import importlib
import logging
import os
import types
import warnings
from functools import cache

from cimprofiles import profile_module
# The model-scope getters live in cimprofiles because Identity reads them. Import, never copy:
# set_model_scope() must clear the same @cache that Identity uses.
from cimprofiles.env_vars import (DEFAULT_MODEL_AUTHORITY, DEFAULT_MODEL_NAME,
                                  DEFAULT_VALIDATION_LOG_LEVEL, get_model_authority,
                                  get_model_name, get_validation_log_level)

_log = logging.getLogger(__name__)

# Memo for merged modules: spec string → ModuleType.
# Keyed outside @cache so it survives cache_clear() calls from connection __init__.
_merge_memo: dict[str, types.ModuleType] = {}

DEFAULT_NAMESPACE = 'http://iec.ch/TC57/CIM100#'
DEFAULT_CIM_PROFILE = 'cim18v17'
DEFAULT_URL = 'http://localhost:8889/bigdata/namespace/kb/sparql'
DEFAULT_DATABASE = 'powergridmodel'
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 61613
DEFAULT_USERNAME = 'system'
DEFAULT_PASSWORD = 'manager'
DEFAULT_IEC61970_301 = 8
DEFAULT_IEC61970_552 = '552-NEW'
IEC61970_552_STYLES = ('552-NEW', '552-LEGACY', 'CGMES')
DEFAULT_USE_UNITS = 'true'
DEFAULT_ALLOW_UNDEFINED_ATTRIBUTES = 'false'
DEFAULT_MVA_BASE = 100

_LEGACY_PROFILE_PREFIX = 'cimgraph.data_profile.'


def _qualify(path: str) -> str:
    """
    Returns the full module path of a profile. A short name, optionally with a
    sub-profile ('cimhub_2023', 'cim18gmdm.connectivity'), is looked up in
    cimprofiles.PROFILE_PACKAGES, and so is a pre-0.6 'cimgraph.data_profile.' path,
    so every spelling gives the same module and the same merge-memo key (otherwise
    two spellings would build two sets of merged classes whose objects miss each
    other's graph keys).
    """
    if path.startswith('cimprofiles.'):
        return path
    if path.startswith(_LEGACY_PROFILE_PREFIX):
        qualified = profile_module(path[len(_LEGACY_PROFILE_PREFIX):])
        warnings.warn(f'CIMG_CIM_PROFILE path {path!r} is deprecated; use {qualified!r}',
                      DeprecationWarning, stacklevel=3)
        return qualified
    return profile_module(path)


@cache
def get_cim_profile() -> tuple[str, types.ModuleType]:
    """Return (cim_profile_str, cim_module) for the active CIM profile.

    CIMG_CIM_PROFILE may be:
    - A single profile: 'cimhub_2023' or 'cimprofiles.cim17.cimhub_2023'
    - A comma-separated list of sub-profiles that are merged at runtime:
      'cim18gmdm.connectivity,cim18gmdm.electrical'

    The pre-0.6 'cimgraph.data_profile.' paths are still accepted.

    Merged modules are memoised in _merge_memo (not in the @cache) so that the
    same spec string always returns the same module object even when cache_clear()
    is called by a connection __init__.
    """
    cim_profile = os.getenv('CIMG_CIM_PROFILE')
    if cim_profile is None:
        raise ValueError('CIMG_CIM_PROFILE environment variable is not set.')

    parts = [_qualify(p.strip()) for p in cim_profile.split(',') if p.strip()]

    if len(parts) == 1:
        cim = importlib.import_module(parts[0])
        return cim_profile, cim

    # Comma-spec: build or retrieve a merged module.
    spec_key = ','.join(parts)
    if spec_key not in _merge_memo:
        from cimprofiles.merge import merge_profiles
        mods = [importlib.import_module(p) for p in parts]
        _merge_memo[spec_key] = merge_profiles(*mods)
    return spec_key, _merge_memo[spec_key]

@cache
def get_namespace() -> str:
    """
    Returns the namespace for the cimgraph database
    Returns:
        namespace: the namespace for the cimgraph database
    """
    namespace = os.getenv('CIMG_NAMESPACE')
    if namespace is None:
        namespace = DEFAULT_NAMESPACE
        _log.debug('Default namespace for CIM100 used')
        # raise ValueError('CIMG_NAMESPACE environment variable is not set.')
    return namespace

@cache
def get_iec61970_552() -> str:
    """Return the IEC 61970-552 serialization format for this session.

    Reads ``CIMG_IEC61970_552`` (preferred) or the legacy ``CIMG_IEC61970_301``.

    Returns:
        ``'552-NEW'``    — ``rdf:about="urn:uuid:<uuid>"``, mRID ``<uuid>`` (IEC 61970-552 ed. 2,
        default)
        ``'552-LEGACY'`` — ``rdf:ID="_<uuid>"``, references ``#_<uuid>``, mRID ``_<uuid>``
        (IEC 61970-552 ed. 1)
        ``'CGMES'``      — ``rdf:ID="_<uuid>"``, references ``#_<uuid>``, mRID ``<uuid>``
    """
    val = os.getenv('CIMG_IEC61970_552')
    if val is not None:
        val = val.strip()
        if val not in IEC61970_552_STYLES:
            raise ValueError(
                f'CIMG_IEC61970_552 must be one of {IEC61970_552_STYLES}, got {val!r}'
            )
        return val

    # Fall back to the old integer env var with a deprecation warning.
    legacy = os.getenv('CIMG_IEC61970_301')
    if legacy is not None:
        warnings.warn(
            'CIMG_IEC61970_301 is deprecated and will be removed in a future release. '
            "Use CIMG_IEC61970_552='552-NEW' or '552-LEGACY' instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        try:
            return '552-NEW' if int(legacy) > 7 else '552-LEGACY'
        except ValueError:
            raise ValueError(
                f"Legacy CIMG_IEC61970_301 must be an integer, got {legacy!r}"
            )

    return DEFAULT_IEC61970_552


def get_iec61970_301() -> int:
    """Deprecated. Use ``get_iec61970_552()`` instead.

    Returns the old integer encoding (8 for 552-NEW, 7 for 552-LEGACY) for
    callers that have not yet migrated.
    """
    warnings.warn(
        'get_iec61970_301() is deprecated. Use get_iec61970_552() instead.',
        DeprecationWarning,
        stacklevel=2,
    )
    return 8 if get_iec61970_552() == '552-NEW' else 7


@cache
def get_url() -> str:
    """
    Returns the URL for the cimgraph database
    Returns:
        url: the URL for the cimgraph database
    """
    url = os.getenv('CIMG_URL')
    if url is None:
        _log.warning('CIMG_URL environment variable is not set. Using Blazegraph default')
        url = DEFAULT_URL
        # raise ValueError('CIMG_URL environment variable is not set.')
    return url

@cache
def get_database() -> str:
    """
    Returns the database name for the cimgraph database
    Returns:
        database: the database name for the cimgraph database
    """
    database = os.getenv('CIMG_DATABASE')
    if database is None:
        _log.warning('CIMG_DATABASE environment variable is not set.')
        database = DEFAULT_DATABASE
        # raise ValueError('CIMG_DATABASE environment variable is not set.')
    return database

@cache
def get_use_units() -> bool:
    """
    Returns the use_units flag for the cimgraph database
    Returns:
        use_units: the use_units flag for the cimgraph database
    """
    use_units = os.getenv('CIMG_USE_UNITS')
    if use_units is None:
        use_units = DEFAULT_USE_UNITS
        _log.debug('CIMG_USE_UNITS environment variable is not set. Defaulting to false.')
    return use_units.lower() == 'true'

@cache
def get_username() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        username: str
    """
    username = os.getenv('CIMG_USERNAME')
    if username is None:
        _log.warning('CIMG_USERNAME environment variable is not set.')
        username = DEFAULT_USERNAME
    return username

@cache
def get_password() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        password: str
    """
    password = os.getenv('CIMG_PASSWORD')
    if password is None:
        _log.warning('CIMG_PASSWORD environment variable is not set.')
        password = DEFAULT_PASSWORD
    return password

@cache
def get_host() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        host: str
    """
    host = os.getenv('CIMG_HOST')
    if host is None:
        _log.warning('CIMG_HOST environment variable is not set.')
        host = DEFAULT_HOST
    return host

@cache
def get_port() -> int:
    port = os.getenv('CIMG_PORT')
    if port is None:
        _log.warning('CIMG_PORT environment variable is not set.')
        return DEFAULT_PORT
    return int(port)

@cache
def get_undefined_handling() -> str:
    '''
    Returns the log level used for validation warnings
    Returns:
        log_level: str
    '''
    handling = os.environ.get('CIMG_ALLOW_UNDEFINED_ATTRIBUTES',
                        DEFAULT_ALLOW_UNDEFINED_ATTRIBUTES)
    return handling.lower() == 'true'

def set_model_scope(authority: str, model_name: str) -> None:
    """
    Sets CIMG_MODEL_AUTHORITY and CIMG_MODEL_NAME so that UUIDs seeded from now on,
    and the header of the next export, use this model authority and model name.
    """
    if (authority, model_name) != (get_model_authority(), get_model_name()):
        _log.info(f'Setting model scope to authority {authority!r}, model name {model_name!r}')
    os.environ['CIMG_MODEL_AUTHORITY'] = authority
    os.environ['CIMG_MODEL_NAME'] = model_name
    get_model_authority.cache_clear()
    get_model_name.cache_clear()


@cache
def get_system_mva_base() -> float:
    """Sets sytem-wide MVA base needed for per-unit <--> ohm conversion
    """
    value = float(os.getenv('CIMG_SYSTEM_MVA_BASE'))
    if value is None:
        _log.warning('CIMG_SYSTEM_MVA_BASE environment variable is not set. Using 100 MVA default')
        value = DEFAULT_MVA_BASE
    return value