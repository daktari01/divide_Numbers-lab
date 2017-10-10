""" Test our divideNumbers function """

import unittest

from divideNumbers import divideNumbers

class TestDivideNumbers(unittest.TestCase):
    """Test divideNumbers functionality"""
    def test_division(self):
        self.assertEqual(divideNumbers(10, 5), 2)
        self.assertEqual(divideNumbers(-1, 1), -1)
        self.assertEqual(divideNumbers(5, 2), 2.5)
        
    def test_raises_exception(self):
        with self.assertRaises(ValueError):
            divideNumbers(4, 0)
        
    def test_input_is_not_a_list(self):
        with self.assertRaises(TypeError):
            divideNumbers([2, 3], [1,2])
            divideNumbers([2, 3], 3)
            divideNumbers(4, [1,2])
        
if __name__ == '__main__':
    unittest.main()
