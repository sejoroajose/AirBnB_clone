#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Unittests for the City class."""

    def test_initialization(self):
        """Test initialization of City instance."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_update_attribute(self):
        """Test updating attributes of City instance."""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_str_representation(self):
        """Test string representation of City instance."""
        city = City()
        city.state_id = "NY"
        city.name = "New York"
        self.assertEqual(str(city), "[City] ({}) {}".format(city.id, city.__dict__))

    # Add more test cases as needed...

if __name__ == "__main__":
    unittest.main()
