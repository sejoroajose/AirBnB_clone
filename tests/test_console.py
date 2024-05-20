#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    """Unittests for the HBNBCommand class."""

    def setUp(self):
        """Set up test environment."""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment."""
        storage._FileStorage__objects = {}

    @patch('sys.stdout', new=StringIO())
    def test_create(self, mock_stdout):
        """Test create command."""
        HBNBCommand().onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)
        self.assertIn("User." + output, storage.all().keys())

    @patch('sys.stdout', new=StringIO())
    def test_show(self, mock_stdout):
        """Test show command."""
        HBNBCommand().onecmd("create User")
        user_id = mock_stdout.getvalue().strip()
        HBNBCommand().onecmd(f"show User {user_id}")
        output = mock_stdout.getvalue().strip().split('\n')[1]
        self.assertIn(f"User.{user_id}", output)

    @patch('sys.stdout', new=StringIO())
    def test_destroy(self, mock_stdout):
        """Test destroy command."""
        HBNBCommand().onecmd("create User")
        user_id = mock_stdout.getvalue().strip()
        HBNBCommand().onecmd(f"destroy User {user_id}")
        self.assertNotIn(f"User.{user_id}", storage.all().keys())

    @patch('sys.stdout', new=StringIO())
    def test_all(self, mock_stdout):
        """Test all command."""
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("all User")
        output = mock_stdout.getvalue().strip().split('\n')[1]
        self.assertIn("[User]", output)

    @patch('sys.stdout', new=StringIO())
    def test_update(self, mock_stdout):
        """Test update command."""
        HBNBCommand().onecmd("create User")
        user_id = mock_stdout.getvalue().strip()
        HBNBCommand().onecmd(f"update User {user_id} first_name John")
        HBNBCommand().onecmd(f"show User {user_id}")
        output = mock_stdout.getvalue().strip().split('\n')[2]
        self.assertIn("'first_name': 'John'", output)

    @patch('sys.stdout', new=StringIO())
    def test_count(self, mock_stdout):
        """Test count command."""
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("User.count()")
        output = mock_stdout.getvalue().strip().split('\n')[2]
        self.assertEqual(output, "2")

    @patch('sys.stdout', new=StringIO())
    def test_update_with_dict(self, mock_stdout):
        """Test update command with a dictionary."""
        HBNBCommand().onecmd("create User")
        user_id = mock_stdout.getvalue().strip()
        HBNBCommand().onecmd(f'User.update("{user_id}", {{"first_name": "John", "age": 30}})')
        HBNBCommand().onecmd(f"show User {user_id}")
        output = mock_stdout.getvalue().strip().split('\n')[2]
        self.assertIn("'first_name': 'John'", output)
        self.assertIn("'age': 30", output)

    @patch('sys.stdout', new=StringIO())
    def test_show_no_id(self, mock_stdout):
        """Test show command without ID."""
        HBNBCommand().onecmd("show User")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new=StringIO())
    def test_show_no_class(self, mock_stdout):
        """Test show command without class name."""
        HBNBCommand().onecmd("show")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new=StringIO())
    def test_show_no_instance_found(self, mock_stdout):
        """Test show command with nonexistent instance."""
        HBNBCommand().onecmd("show User 12345")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new=StringIO())
    def test_destroy_no_id(self, mock_stdout):
        """Test destroy command without ID."""
        HBNBCommand().onecmd("destroy User")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new=StringIO())
    def test_destroy_no_class(self, mock_stdout):
        """Test destroy command without class name."""
        HBNBCommand().onecmd("destroy")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new=StringIO())
    def test_destroy_no_instance_found(self, mock_stdout):
        """Test destroy command with nonexistent instance."""
        HBNBCommand().onecmd("destroy User 12345")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

if __name__ == "__main__":
    unittest.main()
