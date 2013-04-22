import unittest
from FizzBuzzGame import FizzBuzzGame 


class TestFizzBuzzNumber(unittest.TestCase):

    def testFirstFizzBuzzNumberShouldBeOne(self):
        self.assertEquals('1', self.getfizzBuzzValueOf(1))

    def testSecondFizzBuzzNumberShouldBeTwo(self):
        self.assertEquals('2', self.getfizzBuzzValueOf(2))

    def testThirdFizzBuzzNumberShouldBeFizz(self):
        self.assertEquals("Fizz", self.getfizzBuzzValueOf(3))

    def testFifthFizzBuzzNumberShouldBeBuzz(self):
        self.assertEquals("Buzz", self.getfizzBuzzValueOf(5))

    def testSixthFizzBuzzNumberShouldBeFizz(self):
        self.assertEquals("Fizz", self.getfizzBuzzValueOf(6))

    def testTenFizzBuzzNumberShouldBeBuzz(self):
        self.assertEquals("Buzz", self.getfizzBuzzValueOf(10))

    def testFifteenFizzBuzzNumberShouldBeFizzBuzz(self):
        self.assertEquals("FizzBuzz", self.getfizzBuzzValueOf(15))

    def getfizzBuzzValueOf(self, number):
        return FizzBuzzGame().getFizzBuzzNumber(number)
    
    
    
    
    def testFizzBuzzSequenceOfLengthOneShouldBeStringOne(self):
        self.assertEquals("1", self.getFizzbuzzSequenceOfLength(1))

    def testFizzBuzzSequenceOfLengthTwoShouldBeStringOneCommaTwo(self):
        self.assertEquals("1,2", self.getFizzbuzzSequenceOfLength(2))

    def testFizzBuzzSequenceOfLengthThreeShouldBeStringOneCommaTwoCommaFizz(self):
        self.assertEquals("1,2,Fizz", self.getFizzbuzzSequenceOfLength(3))

    def getFizzbuzzSequenceOfLength(self, length):
        return FizzBuzzGame().getFizzBuzzSequence(length)
        

#suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzzNumber)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzzSequence)
#unittest.TextTestRunner(verbosity=1).run(suite1)
#unittest.TextTestRunner(verbosity=1).run(suite2)
