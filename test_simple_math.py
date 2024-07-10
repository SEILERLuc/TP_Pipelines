"""
Module for testing the SimpleMath class.
"""

import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    """
    Class for testing the SimpleMath class.
    """

    def test_addition(self):
        """
        Test addition
        """
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8, "Addition of 3 and 5 should be 8")

        result = SimpleMath.addition(-3, -5)
        self.assertEqual(result, -8, "Addition of -3 and -5 should be -8")

        result = SimpleMath.addition(10, -5)
        self.assertEqual(result, 5, "Addition of 10 and -5 should be 5")

        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0, "Addition of 0 and 0 should be 0")
    
    def test_substraction(self):
        """
        Test the subtraction function of the SimpleMath class.

        This function tests the subtraction function of the SimpleMath class. 
        It verifies that the function correctly subtracts two numbers and 
        returns the expected result.

        Parameters:
            self (TestSimpleMath): The current test case.

        Returns:
            None
        """
        result = SimpleMath.substraction(10, 3)
        self.assertEqual(result, 7, "Subtraction of 10 and 3 should be 7")

        result = SimpleMath.substraction(-5, -2)
        self.assertEqual(result, -3, "Subtraction of -5 and -2 should be -3")

        result = SimpleMath.substraction(5, -3)
        self.assertEqual(result, 8, "Subtraction of 5 and -3 should be 8")

        result = SimpleMath.substraction(0, 0)
        self.assertEqual(result, 0, "Subtraction of 0 and 0 should be 0")

if __name__ == '__main__':
    unittest.main()
