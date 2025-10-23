import unittest
from main import MyApp, MyGrid

class TestApp(unittest.TestCase):
    def test_app_creation(self):
        app = MyApp()
        self.assertIsNotNone(app)

    def test_grid_creation(self):
        grid = MyGrid()
        self.assertIsNotNone(grid)

if __name__ == '__main__':
    unittest.main()
