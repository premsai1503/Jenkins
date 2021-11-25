#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from IMT2019067_prog import power

class Test_power(unittest.TestCase):
    def test_1(self):
        data = [2,4]
        result = power(2,4)
        self.assertEqual(result, 16)
    def test_2(self):
        data = [64,0.5]
        result = power(64,0.5)
        self.assertEqual(result, 8)
        
    def test_1(self):
        data = [9,2]
        result = power(9,2)
        self.assertEqual(result, 81)

if __name__ == '__main__':
    unittest.main()
