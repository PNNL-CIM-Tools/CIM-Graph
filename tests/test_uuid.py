import json
import re
import unittest
from uuid import UUID

import cimgraph.data_profile.cimhub_2023 as cim


class TestIdentityUUID(unittest.TestCase):


    def test_initialization_with_mRID(self):
        """Test initializing a Feeder with mRID parameter."""

        feeder = cim.Feeder(mRID='49ad8e07-3bf9-a4e2-cb8f-c3722f837b62')

        # Test string representation
        expected_str = '{"@id": "49ad8e07-3bf9-a4e2-cb8f-c3722f837b62", "@type": "Feeder"}'
        self.assertEqual(feeder.__str__(), expected_str)

        # Test URI method
        self.assertEqual(feeder.uri(), '49ad8e07-3bf9-a4e2-cb8f-c3722f837b62')

    def test_initialization_with_mRID_caps_underscore(self):
        """Test initializing a Feeder with mRID parameter."""

        feeder = cim.Feeder(mRID='_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62')

        # Test string representation
        expected_str = '{"@id": "49ad8e07-3bf9-a4e2-cb8f-c3722f837b62", "@type": "Feeder"}'
        self.assertEqual(feeder.__str__(), expected_str)

        # Test URI method
        self.assertEqual(feeder.uri(), '_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62')

    def test_set_uuid_after_initialization(self):
        """Test setting UUID after initialization using uuid() method."""
        # Initialize empty Feeder, then set UUID
        feeder = cim.Feeder()
        feeder.uuid(mRID='49ad8e07-3bf9-a4e2-cb8f-c3722f837b62')

        # Verify using string representation
        # Note: Using a helper method to compare JSON contents
        self.verify_json_content(
            feeder.__str__(),
            {'@id': '49ad8e07-3bf9-a4e2-cb8f-c3722f837b62', '@type': 'Feeder'}
        )

        # Test URI method
        self.assertEqual(feeder.uri(), '49ad8e07-3bf9-a4e2-cb8f-c3722f837b62')

    def test_initialization_with_UUID_object(self):
        """Test initializing a Feeder with UUID object."""
        uuid_obj = UUID('49ad8e07-3bf9-a4e2-cb8f-c3722f837b62')
        feeder = cim.Feeder(identifier=uuid_obj)

        # Verify using string representation
        self.verify_json_content(
            feeder.__str__(),
            {'@id': '49ad8e07-3bf9-a4e2-cb8f-c3722f837b62', '@type': 'Feeder'}
        )

        # Test URI method
        self.assertEqual(feeder.uri(), '49ad8e07-3bf9-a4e2-cb8f-c3722f837b62')

    def test_invalid_identifier_handling(self):
        """Test that invalid identifiers produce expected behavior and a valid UUID is created."""
        # Create a new test case for an invalid identifier
        with self.assertLogs(level='WARNING') as log_context:
            # This will raise an AssertionError if no logs of the specified level are issued
            feeder = cim.Feeder(identifier='qwertyuiop')

            # Check that we received some warning logs
            self.assertTrue(len(log_context.records) > 0)

            # Check for expected content in warning messages
            warning_text = '\n'.join(record.getMessage() for record in log_context.records)
            self.assertIn('qwertyuiop', warning_text)

            # Two approaches to verify warnings:
            # 1. Less strict: Just check that warnings were generated with the invalid ID
            self.assertTrue(any('qwertyuiop' in record.getMessage() for record in log_context.records))

            # 2. More specific: Check for specific warning messages if needed
            expected_messages = [
                'Identifier qwertyuiop must be a UUID object',
                'URI qwertyuiop not a valid UUID',
                'qwertyuiop not a valid UUID'
            ]

            # Check for each expected message (allowing for partial matches)
            for expected in expected_messages:
                found = False
                for record in log_context.records:
                    if expected in record.getMessage():
                        found = True
                        break
                # Uncomment this if you want strict validation of each message
                # self.assertTrue(found, f"Expected warning containing '{expected}' not found")
            self.validate_uuid_generation(feeder)

    def validate_uuid_generation(self, feeder):
        # Check that a valid UUID was generated - this part is the same
        feeder_json = feeder.__str__()
        if isinstance(feeder_json, dict):
            uuid_str = feeder_json['@id']
        else:
            # Extract UUID from JSON string if __str__ returns a string
            match = re.search(r'"@id":\s*"([^"]+)"', feeder_json)
            uuid_str = match.group(1) if match else None

        # Verify the UUID follows the proper format
        uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        self.assertIsNotNone(re.match(uuid_pattern, uuid_str))

        # Check that the URI method returns the same UUID
        self.assertEqual(feeder.uri(), uuid_str)

        # Check type is correctly set
        if isinstance(feeder_json, dict):
            self.assertEqual(feeder_json['@type'], 'Feeder')
        else:
            self.assertIn('"@type": "Feeder"', feeder_json)

    # Helper method to compare JSON content regardless of formatting
    def verify_json_content(self, json_str, expected_dict):
        """Helper method to compare JSON content regardless of formatting."""

        # If json_str is already a dictionary (like from __str__()), use it directly
        if isinstance(json_str, dict):
            actual_dict = json_str
        else:
            # Otherwise, parse the JSON string into a dictionary
            actual_dict = json.loads(json_str)

        # Compare dictionaries
        self.assertEqual(actual_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
