import unittest
from methods import *
from sample_functions import *
from function import Function

# TODO: Think of possible test cases
class TestMethods(unittest.TestCase):

    def setUp(self):
        self.func = Function(task_func, -2, 2, 0)
        self.e = 1e-1
    
    def test_dichotomy(self):
        output = dichotomy(self.func.f, self.func.a, self.func.b, self.e)
        self.assertLessEqual(abs(self.func.x0 - output[0]), self.e) # check if precision reached
        self.assertEqual(output[2], output[1] * 2) # check if function lookups twice as iterations number

    def test_golden_ratio(self):
        output = golden_ratio(self.func.f, self.func.a, self.func.b, self.e)
        self.assertLessEqual(abs(self.func.x0 - output[0]), self.e) # check if precision reached
        self.assertEqual(output[2], output[1] + 1) # check if function lookups one more than iterations number

    def test_fibonacci(self):
        output = fibonacci(self.func.f, self.func.a, self.func.b, self.e)
        self.assertLessEqual(abs(self.func.x0 - output[0]), self.e) # check if precision reached
        self.assertEqual(output[2], output[1] + 1) # check if function lookups one more than iterations number

    def test_parabolic(self):
        output = parabolic(self.func.f, self.func.a, self.func.b, self.e)
        self.assertLessEqual(abs(self.func.x0 - output[0]), self.e) # check if precision reached

    def test_brent(self):
        output = brent(self.func.f, self.func.a, self.func.b, self.e)
        self.assertLessEqual(abs(self.func.x0 - output[0]), self.e) # check if precision reached

if __name__ == "__main__":
  unittest.main()