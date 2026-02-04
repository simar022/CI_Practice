import unittest
from app import add_numbers

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
