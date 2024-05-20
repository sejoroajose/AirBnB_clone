#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Unittests for the Amenity class."""

    def test_initialization(self):
        """Test initialization of Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_update_attribute(self):
        """Test updating attribute of Amenity instance."""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    def test_str_representation(self):
        """Test string representation of Amenity instance."""
        amenity = Amenity()
        amenity.name = "Gym"
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__))

    # Add more test cases as needed...

if __name__ == "__main__":
    unittest.main()
