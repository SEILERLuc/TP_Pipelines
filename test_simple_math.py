import unittest
import simple_math.simple_math as SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8, "Addition of 3 and 5 should be 8")

        result = SimpleMath.addition(-3, -5)
        self.assertEqual(result, -8, "Addition of -3 and -5 should be -8")

        result = SimpleMath.addition(10, -5)
        self.assertEqual(result, 5, "Addition of 10 and -5 should be 5")

        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0, "Addition of 0 and 0 should be 0")

if __name__ == '__main__':
    # unittest.main()
    print(SimpleMath.addition(3, 5))



    # sm = SimpleMath()
    # res = SimpleMath.addition(3, 5)
    # print(res)
    # print(sm.addition(3, 5))