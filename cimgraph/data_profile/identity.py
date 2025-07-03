import json
import logging
from dataclasses import dataclass, field, is_dataclass
from enum import Enum
from random import Random
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

# Global configuration
ARCHIVE_JSON_LD = True
_log = logging.getLogger(__name__)

class CIMStereotype(Enum):
    Abstract = 'Abstract'
    Concrete = 'Concrete'
    Description = 'Description'
    Compound = 'Compound'
    AggregateOf = 'AggregateOf'
    OfAggregate = 'OfAggregate'
    Attribute = 'Attribute'
    CIMDatatype = 'CIMDatatype'
    Enumeration = 'Enumeration'
    ByReference = 'ByReference'

def stereotype(stereotype: CIMStereotype):
    """Decorator to add UML stereotype metadata to dataclasses"""
    def decorator(cls):
        cls.__stereotype__ = stereotype
        return cls
    return decorator

class UUID_Meta:
    """
    Helper class for managing UUID generation and metadata about the original identifiers.

    This class maintains information about how URIs and mRIDs were formatted in the
    source data to preserve capitalization and underscore conventions when needed.
    """

    def __init__(self):
        """Initialize UUID metadata attributes."""
        self.uuid: Optional[UUID] = None
        self.uuid_str: str = ''
        self.uri_has_underscore: bool = False
        self.uri_is_capitalized: bool = False
        self.mrid_has_underscore: bool = False
        self.mrid_is_capitalized: bool = False

    def generate_uuid(self, mRID: Optional[str] = None, uri: Optional[str] = None,
                    name: Optional[str] = None, seed: Optional[str] = None) -> UUID:
        """
        Generate a consistent UUID from various input formats.

        Tries to create a UUID from a URI or mRID if possible, or generates a new one
        based on the provided seed or randomly if no valid inputs are available.

        Args:
            mRID: An mRID string that might be convertible to a UUID
            uri: A URI string that might be convertible to a UUID
            name: A name to use in seed generation
            seed: Additional seed information for UUID generation

        Returns:
            UUID: The generated UUID object
        """
        if seed is None:
            seed = ''

        invalid_mrid = True

        # Try creating UUID from URI first
        if uri is not None:
            # Track formatting characteristics
            if uri.strip('_') != uri:
                self.uri_has_underscore = True
            if uri.lower() != uri:
                self.uri_is_capitalized = True

            try:
                # Convert URI to UUID directly if possible
                self.uuid = UUID(uri.strip('_').lower())
                invalid_mrid = False
            except ValueError:
                # If URI is not a valid UUID, use it as seed
                seed = seed + uri
                _log.warning(f'URI {uri} not a valid UUID, generating new UUID')
                mRID = str(uri)

        # Try creating UUID from mRID if URI failed or wasn't provided
        if mRID is not None:
            # Track formatting characteristics
            if mRID.strip('_') != mRID:
                self.mrid_has_underscore = True
                if uri is None:
                    self.uri_has_underscore = True

            if mRID.lower() != mRID:
                self.mrid_is_capitalized = True
                if uri is None:
                    self.uri_is_capitalized = True

            # Try to create UUID from mRID if we don't have one yet
            if self.uuid is None:
                try:
                    self.uuid = UUID(mRID.strip('_').lower())
                    invalid_mrid = False
                except ValueError:
                    # If mRID is not a valid UUID, add to seed
                    seed = seed + mRID

        # If we couldn't create a UUID from inputs, generate a new one
        if invalid_mrid:
            if seed:
                # Generate a deterministic UUID from the seed
                random_generator = Random(seed)
                self.uuid = UUID(int=random_generator.getrandbits(128), version=4)
            else:
                # Generate a completely random UUID
                self.uuid = uuid4()

        # Store string representation
        self.uuid_str = str(self.uuid)
        return self.uuid


@dataclass
class Identity:
    """
    Base class for CIM 18 identity management.

    This is the root class from CIM 18 to provide common identification
    for all classes needing identification and naming attributes.
    IdentifiedObject is now a child class of Identity.
    mRID is superseded by Identity.identifier, which is typed to be a UUID.
    """

    identifier: Optional[UUID] = field(
        default=None,
        metadata={
            'type': 'Attribute',
            'minOccurs': '1',
            'maxOccurs': '1'
        })

    def __post_init__(self) -> None:
        """
        Initializes the UUID after dataclass instantiation.

        Ensures that the identifier field is a valid UUID, creating one from
        other available identification fields if necessary.
        """
        # Internal tracking attribute for JSON-LD representation
        self.__uuid__ = None
        self.__json_ld__ = None

        # Initialize identifier
        if self.identifier is not None:
            # Handle inheriting from IdentifiedObject with mRID field
            if 'mRID' in self.__dataclass_fields__:
                self.uuid(uri=str(self.identifier),
                         mRID=getattr(self, 'mRID', None),
                         name=getattr(self, 'name', None))
            else:
                self.uuid(uri=str(self.identifier))
        else:
            # Create new identifier
            if 'mRID' in self.__dataclass_fields__:
                self.uuid(mRID=getattr(self, 'mRID', None),
                         name=getattr(self, 'name', None))
            else:
                self.uuid()

    def __str__(self, show_mRID: bool = False, show_empty: bool = False,
                use_names: bool = False) -> str:
        """
        Provides a JSON string representation of the object.

        Args:
            show_mRID: Whether to include mRID and identifier in output
            show_empty: Whether to include empty/None attributes
            use_names: Whether to use names instead of full representation for nested objects

        Returns:
            str: JSON string representation of the object
        """
        # Create JSON-LD dump with repr and all attributes
        dump = dict(json.loads(self.__repr__()) | self.__dict__)

        # Remove internal attributes
        dump.pop('__uuid__', None)
        dump.pop('__json_ld__', None)

        # Process each attribute
        for attribute in self.__dataclass_fields__:
            # Delete attributes that are empty when show_empty is False
            if attribute in dump and (dump[attribute] is None or dump[attribute] == []):
                if not show_empty:
                    del dump[attribute]
                continue

            # Handle dataclass attributes
            if attribute in dump and is_dataclass(dump[attribute]):
                if use_names and hasattr(dump[attribute], 'name'):
                    dump[attribute] = dump[attribute].name
                else:
                    dump[attribute] = dump[attribute].__repr__()

            # Convert non-string attributes to strings for JSON compatibility
            elif attribute in dump and not isinstance(dump[attribute], str):
                dump[attribute] = str(dump[attribute])

        # Remove identifier and mRID if not showing them
        if not show_mRID:
            dump.pop('identifier', None)
            dump.pop('mRID', None)

        # Convert to JSON with proper formatting
        json_str = json.dumps(dump)

        # Fix common JSON formatting issues
        replacements = [
            ('\\\"', '\"'),
            ('\"[', '['),
            (']\"', ']'),
            ('\"{', '{'),
            ('}\"', '}')
        ]

        for old, new in replacements:
            json_str = json_str.replace(old, new)

        return json_str

    def __repr__(self) -> str:
        """
        Returns a minimal JSON-LD representation of the object.

        Avoids infinite recursion when printing nested objects by providing
        only type and identifier information.

        Returns:
            str: Minimal JSON-LD representation
        """
        if ARCHIVE_JSON_LD:
            return self.__json_ld__
        else:
            return json.dumps({
                '@id': f'{str(self.identifier)}',
                '@type': f'{self.__class__.__name__}'
            })

    def pprint(self, print_mRID: bool = False) -> None:
        """
        Pretty prints the object as formatted JSON.

        Args:
            print_mRID: Whether to include mRID in the output
        """
        print(json.dumps(json.loads(self.__str__(print_mRID)), indent=4))

    def uuid(self, mRID: Optional[str] = None, uri: Optional[str] = None,
             name: Optional[str] = None, seed: Optional[str] = None) -> UUID:
        """
        Creates or updates the object's UUID.

        Args:
            mRID: An mRID string that might be convertible to a UUID
            uri: A URI string that might be convertible to a UUID
            name: A name to use in seed generation
            seed: Additional seed information for UUID generation

        Returns:
            UUID: The generated or updated UUID
        """
        # Initialize UUID metadata
        self.__uuid__ = UUID_Meta()

        # Prepare seed if needed
        if seed is None:
            seed = ''

        # Add class and name information to seed if available
        if name is not None:
            seed = seed + f'{self.__class__.__name__}:{name}'

        # Generate UUID using UUID_Meta helper
        self.identifier = self.__uuid__.generate_uuid(
            mRID=mRID, uri=uri, name=name, seed=seed)

        # Update mRID for backwards compatibility
        if 'mRID' in self.__dataclass_fields__:
            if mRID is not None:
                self.mRID = mRID
            else:
                self.mRID = str(self.identifier)

            # Update name if provided
            if name is not None:
                self.name = name

        # Store JSON-LD representation if configured
        if ARCHIVE_JSON_LD:
            self.__json_ld__ = json.dumps({
                '@id': f'{str(self.identifier)}',
                '@type': f'{self.__class__.__name__}'
            })

        return self.identifier

    def uri(self) -> str:
        """
        Returns the URI form of the identifier, respecting original formatting.

        Returns:
            str: The URI string representation with original capitalization and underscores
        """
        uri = str(self.identifier)

        # Apply original formatting if available
        try:
            if self.__uuid__.uri_is_capitalized:
                uri = uri.upper()
            if self.__uuid__.uri_has_underscore:
                uri = '_' + uri
        except (AttributeError, TypeError):
            # If __uuid__ is not available, use the identifier as is
            pass

        return uri

    def to_json(self, show_mRID: bool = True, show_empty: bool = True,
               use_names: bool = False) -> str:
        """
        Returns a JSON string representation of the object.

        Args:
            show_mRID: Whether to include mRID and identifier
            show_empty: Whether to include empty/None attributes
            use_names: Whether to use names instead of full representation for nested objects

        Returns:
            str: JSON string representation
        """
        return self.__str__(
            show_mRID=show_mRID,
            show_empty=show_empty,
            use_names=use_names
        )

    def to_dict(self, show_mRID: bool = True, show_empty: bool = True,
               use_names: bool = False) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the object.

        Args:
            show_mRID: Whether to include mRID and identifier
            show_empty: Whether to include empty/None attributes
            use_names: Whether to use names instead of full representation for nested objects

        Returns:
            Dict[str, Any]: Dictionary representation
        """
        return json.loads(self.__str__(
            show_mRID=show_mRID,
            show_empty=show_empty,
            use_names=use_names
        ))

    def expand(self, max_items: int = 10) -> Dict[str, Any]:
        """
        Expands the Identity object to a dictionary with limited list items.

        Creates a more detailed representation of the object while limiting
        the size of lists to prevent overwhelming output.

        Args:
            max_items: Maximum number of items to include in list fields

        Returns:
            Dict[str, Any]: Expanded dictionary representation
        """
        # Start with the combination of repr() and __dict__
        dump = dict(json.loads(self.__repr__()) | self.__dict__)

        # Remove internal attributes
        dump.pop('__uuid__', None)
        dump.pop('__json_ld__', None)

        # Process each dataclass field
        for attribute in self.__dataclass_fields__:
            if attribute not in dump:
                continue

            value = dump[attribute]

            # Remove empty attributes
            if value is None or value == []:
                dump.pop(attribute, None)
                continue

            # Handle dataclass values
            elif is_dataclass(value):
                dump[attribute] = json.loads(str(value))
                # Limit any lists within the dataclass
                for k, v in dump[attribute].items():
                    if isinstance(v, list):
                        dump[attribute][k] = v[:max_items]

            # Handle lists - with limit of max_items
            elif isinstance(value, list):
                # Apply item limit
                limited_value = value[:max_items]

                # If list contains dataclasses, expand them too
                if limited_value and all(is_dataclass(item) for item in limited_value):
                    dump[attribute] = [json.loads(str(item)) for item in limited_value]
                else:
                    dump[attribute] = limited_value

            # Convert other types to string
            elif not isinstance(value, str):
                dump[attribute] = str(value)

        return dump
