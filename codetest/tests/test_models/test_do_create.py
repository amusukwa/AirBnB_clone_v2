import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        # Create an instance of the HBNBCommand class for testing
        self.console = HBNBCommand()

    def tearDown(self):
        # Clean up resources if needed
        pass

    def test_create_with_valid_input(self):
        # Test creating an object with valid input
        class_name = 'BaseModel'
        parameters = 'name="TestObject" age=25'
        command = f"create {class_name} {parameters}"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)

        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.isalnum())  # Check if the output is an alphanumeric ID

    def test_create_with_invalid_class(self):
        # Test creating an object with an invalid class
        class_name = 'InvalidClass'
        parameters = 'name="TestObject"'
        command = f"create {class_name} {parameters}"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)

        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_with_missing_class_name(self):
        # Test creating an object with a missing class name
        command = "create"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)

        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()


