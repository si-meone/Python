'''
Created on 26 Nov 2011

@author: default
'''
import unittest

from games import FizzBuzzWizzGenerator

class TestFizzBuzzWhizzGenerator(unittest.TestCase):

    def setUp(self):
        self.fb_gen = FizzBuzzWizzGenerator()

    def test_create_fizz_buzz_generator(self):
        self.assertTrue(self.fb_gen, 'generator not created')
        
    def test_1_generated_should_be_1(self):
        self.assertEqual(1, self.fb_gen(1))

    def test_2_generated_should_be_2(self):
        self.assertEqual(2, self.fb_gen(2))

    def test_letter_input_causes_value_exception(self):
        self.assertRaises(ValueError, self.fb_gen, 'a')
        
    def test_3__generated_should_be_fizz(self):
        self.assertEquals('fizz', self.fb_gen(3))

    def test_5__generated_should_be_buzz(self):
        self.assertEquals('buzz', self.fb_gen(5))

    def test_6__generated_should_be_fizz(self):
        self.assertEquals('fizz', self.fb_gen(6))
        
    def test_10__generated_should_be_buzz(self):
        self.assertEquals('fizz', self.fb_gen(6))

    def test_15__generated_should_be_wizz(self):
        self.assertEquals('wizz', self.fb_gen(15))
        
if __name__ == '__main__':
    unittest.main()