import unittest

from src.fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3))
    
    def test_fizzbuzz__5_returns_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))
    
    def test_fizzbuzz__15_returns_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(15))
    
    def test_fizzbuzz__8_returns_8(self):
        self.assertEqual("8", fizzbuzz(8))
