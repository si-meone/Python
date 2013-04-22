import unittest
from FibonacciGenerator import FibonacciGenerator

class TestFibonacciGenerator(unittest.TestCase):
    
    def setUp(self):
        self.fg = FibonacciGenerator()

    def testFirstFibonacciNumberShouldBeZero(self):
        self.assertFibonacciNumberAtPosition(0, 0)

    def testSecondFibonacciNumberShouldBeOne(self):
        self.assertFibonacciNumberAtPosition(1, 1)

    def testThirdFibonacciNumberShouldBeOne(self):
        self.assertFibonacciNumberAtPosition(1, 2)

    def testFourthFibonacciNumberShouldBeTwo(self):
        self.assertFibonacciNumberAtPosition(2, 3)

    def testSixthFibonacciNumberShouldBeFour(self):
        self.assertFibonacciNumberAtPosition(5, 5)

    def testWhenSequenceOfSevenFibonacciNumbersRequestedShouldRaiseValueError(self):
        self.assertRaises(ValueError, self.fg.getFibonacciSequence, 7)

    def testWhenSequenceOfTwentyOneFibonacciNumbersRequestedShouldRaiseValueError(self):
        self.assertRaises(ValueError, self.fg.getFibonacciSequence, 21)

    def testWhenSequenceOfEightFibonacciNumbersRequestedShouldGetFirstEightNumbersInSequence(self):
        self.assertEquals([0,1,1,2,3,5,8,13], self.fg.getFibonacciSequence(8))

    def testWhenSequenceOfNineFibonacciNumbersRequestedShouldGetFirstNineNumbersInSequence(self):
        self.assertEquals([0,1,1,2,3,5,8,13,21], self.fg.getFibonacciSequence(9))
    
    #using assert using exected, actual style
    def assertFibonacciNumberAtPosition(self, expectedNumber, position):
        self.assertEquals(expectedNumber, FibonacciGenerator().getFibonacciNumberAtPosition(position))
        
    def tearDown(self):
        del self.fg
    
if __name__ == '__main__':
    unittest.main()

