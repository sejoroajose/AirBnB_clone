#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Unittests for the User class."""

    def test_initialization(self):
        """Test initialization of User instance."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_update_attribute(self):
        """Test updating attributes of User instance."""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_str_representation(self):
        """Test string representation of User instance."""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(str(user), "[User] ({}) {}".format(user.id, user.__dict__))

    # Add more test cases as needed...

if __name__ == "__main__":
    unittest.main()
