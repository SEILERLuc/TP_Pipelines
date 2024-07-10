# tests/test_simple_math.py

import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        # Test case 1: Testing positive numbers
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8, "Addition of 3 and 5 should be 8")

        # Test case 2: Testing negative numbers
        result = SimpleMath.addition(-3, -5)
        self.assertEqual(result, -8, "Addition of -3 and -5 should be -8")

        # Test case 3: Testing a mix of positive and negative numbers
        result = SimpleMath.addition(10, -5)
        self.assertEqual(result, 5, "Addition of 10 and -5 should be 5")

        # Test case 4: Testing with zero
        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0, "Addition of 0 and 0 should be 0")

    
    def test_subtraction(self):
        # Test case 1: Testing positive numbers
        result = SimpleMath.subtraction(10, 3)
        self.assertEqual(result, 7, "Subtraction of 10 and 3 should be 7")

        # Test case 2: Testing negative numbers
        result = SimpleMath.subtraction(-5, -2)
        self.assertEqual(result, -3, "Subtraction of -5 and -2 should be -3")

        # Test case 3: Testing a mix of positive and negative numbers
        result = SimpleMath.subtraction(5, -3)
        self.assertEqual(result, 8, "Subtraction of 5 and -3 should be 8")

        # Test case 4: Testing with zero
        result = SimpleMath.subtraction(0, 0)
        self.assertEqual(result, 0, "Subtraction of 0 and 0 should be 0")

if __name__ == '__main__':
    unittest.main()
