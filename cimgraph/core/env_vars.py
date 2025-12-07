import importlib
import logging
import os


from functools import cache

_log = logging.getLogger(__name__)


DEFAULT_NAMESPACE = 'http://iec.ch/TC57/CIM100#'
DEFAULT_CIM_PROFILE = 'cimhub_2023'
DEFAULT_URL = 'http://localhost:8889/bigdata/namespace/kb/sparql'
DEFAULT_DATABASE = 'powergridmodel'
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = '61613'
DEFAULT_USERNAME = 'system'
DEFAULT_PASSWORD = 'manager'
DEFAULT_IEC61970_301 = 8
DEFAULT_USE_UNITS = 'false'
DEFAULT_VALIDATION_LOG_LEVEL = 'WARNING'
DEFAULT_ALLOW_UNDEFINED_ATTRIBUTES = 'false'

@cache
def get_cim_profile() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        cim_profile: library
    """
    cim_profile = os.getenv('CIMG_CIM_PROFILE')
    if cim_profile is None:
        raise ValueError('CIMG_CIM_PROFILE environment variable is not set.')
    else:
        # try:
            if '.' in cim_profile:
                cim = importlib.import_module(cim_profile)
            else:
                cim = importlib.import_module('cimgraph.data_profile.'+cim_profile)
        # except:
        #     raise ValueError('CIMG_CIM_PROFILE environment variable must be name of a valid object module on the PATH')
    return cim_profile, cim

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
def get_iec61970_301() -> int:
    """
    Returns the IEC61970_301 version for the cimgraph database
    Returns:
        iec61970_301: the IEC61970_301 version for the cimgraph database
    """
    iec61970_301 = os.getenv('CIMG_IEC61970_301')
    if iec61970_301 is None:
        iec61970_301 = DEFAULT_IEC61970_301
        _log.info('CIMG_IEC61970_301 environment variable not set. Defaulting to 8 for urn:uuid:mRID. Set to 7 for mRIDs with underscores')
    else:
        try:
            iec61970_301 = int(iec61970_301)
        except:
            raise ValueError('CIMG_IEC61970_301 environment variable should be an integer')
    return iec61970_301


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
def get_port() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        port: str
    """
    port = os.getenv('CIMG_PORT')
    if port is None:
        _log.warning('CIMG_PORT environment variable is not set.')
        port = DEFAULT_PORT
    return port

@cache
def get_validation_log_level() -> str:
    '''
    Returns the log level used for validation warnings
    Returns:
        log_level: str
    '''
    log_level = getattr(logging, os.environ.get('CIMG_VALIDATION_LOG_LEVEL',
                        DEFAULT_VALIDATION_LOG_LEVEL).upper(), logging.WARNING)
    return log_level

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
