#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from IMT2019067_prog import power

class Test_power(unittest.TestCase):
    def test_1(self):
        data = [2,4]
        result = power(data)
        self.assertEqual(result, 16)
    def test_2(self):
        data = [64,0.5]
        result = power(data)
        self.assertEqual(result, 8)
        
    def test_1(self):
        data = [9,2]
        result = power(data)
        self.assertEqual(result, 80)

if __name__ == '__main__':
    unittest.main()
