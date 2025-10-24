import unittest
import sys
import os

# Add the parent directory to the path so we can import from main.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import MyApp, MyGrid


class TestApp(unittest.TestCase):
    """Test cases for the Kivy application."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = MyApp()
        self.grid = MyGrid()
    
    def test_app_creation(self):
        """Test that the app can be created successfully."""
        self.assertIsNotNone(self.app)
        self.assertIsInstance(self.app, MyApp)

    def test_grid_creation(self):
        """Test that the grid layout can be created successfully."""
        self.assertIsNotNone(self.grid)
        self.assertIsInstance(self.grid, MyGrid)
        
    def test_grid_has_required_widgets(self):
        """Test that the grid contains all required input widgets."""
        # Check that the grid has the expected attributes
        self.assertTrue(hasattr(self.grid, 'name'))
        self.assertTrue(hasattr(self.grid, 'lastName'))
        self.assertTrue(hasattr(self.grid, 'email'))
        self.assertTrue(hasattr(self.grid, 'submit'))
        
    def test_grid_layout_structure(self):
        """Test that the grid has the correct layout structure."""
        # Test that grid has 1 column
        self.assertEqual(self.grid.cols, 1)
        
        # Test that inner grid has 2 columns  
        self.assertEqual(self.grid.inside.cols, 2)


class TestValidation(unittest.TestCase):
    """Test cases for form validation logic."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.grid = MyGrid()
    
    def test_validation_helper_methods(self):
        """Test validation helper methods if they exist."""
        # Note: Since validation is currently in the pressed method,
        # we would need to extract validation logic to separate methods
        # to test it properly. This is a future enhancement.
        pass


if __name__ == '__main__':
    unittest.main()
