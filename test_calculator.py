import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10,3), 30)
        self.assertEqual(mul(5, 5), 25)
        self.assertEqual(mul(10, 2.5), 25)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(6,2), 3)
        self.assertEqual(div(9,3), 3)
        self.assertEqual(div(10,4), 2.5)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        #Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
        # Test basic function
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(36), 6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()