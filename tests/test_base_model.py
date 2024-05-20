#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid
import time

class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

    def test_init(self):
        """Test initialization of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_unique_id(self):
        """Test that each instance has a unique ID."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        model = BaseModel()
        model_str = model.__str__()
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("id", model_str)
        self.assertIn("created_at", model_str)
        self.assertIn("updated_at", model_str)

    def test_save(self):
        """Test the save method of a BaseModel instance."""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.1)  # Ensure the time has passed for updated_at to change
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertLess(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_kwargs(self):
        """Test initialization of a BaseModel instance with kwargs."""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertEqual(new_model.__str__(), model.__str__())

    def test_iso_format(self):
        """Test that created_at and updated_at are strings in iso format in the dictionary representation."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        # Try to parse dates to datetime
        self.assertIsInstance(datetime.fromisoformat(model_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(model_dict['updated_at']), datetime)

    def test_kwargs_invalid(self):
        """Test initialization with invalid kwargs."""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
