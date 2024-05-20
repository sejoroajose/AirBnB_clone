#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """Unittests for the FileStorage class."""

    def setUp(self):
        """Set up for the test."""
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down for the test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """Test adding new object to __objects."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        """Test saving objects to JSON file."""
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test reloading objects from JSON file."""
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)

    # Add more test cases as needed...

if __name__ == "__main__":
    unittest.main()
