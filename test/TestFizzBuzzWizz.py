''' 
Created on 17 May 2010 

@author: nasras01 
''' 
import unittest 
from fizz_buzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase): 



    def testFizzBuzzValueOfIntegerOneShouldBeStringOne(self): 
        self.assertEquals('1', self.getFizzBuzzValueOf(1)) 
        
    def testFizzBuzzValueOfIntegerTwoShouldBeStringTwo(self): 
        self.assertEquals('2', self.getFizzBuzzValueOf(2)) 

    def testFizzBuzzValueOfIntegerThreeShouldBeStringFizz(self): 
        self.assertEquals('fizz', self.getFizzBuzzValueOf(3)) 

    def testFizzBuzzValueOfIntegerFiveShouldBeStringBuzz(self): 
        self.assertEquals('buzz', self.getFizzBuzzValueOf(5)) 
        
    def testFizzBuzzValueOfIntegerSixShouldBeStringFizz(self): 
        self.assertEquals('fizz', self.getFizzBuzzValueOf(6)) 

    def testFizzBuzzValueOfIntegerTenShouldBeStringBuzz(self): 
        self.assertEquals('buzz', self.getFizzBuzzValueOf(10)) 
        
    def testFizzBuzzValueOfIntegerFifteenShouldBeStringFizzBuzz(self): 
        self.assertEquals('fizzbuzz', self.getFizzBuzzValueOf(15)) 

    def getFizzBuzzValueOf(self, number): 
        return FizzBuzz().valueOf(number) 
    
    
    
    
    def testFizzBuzzLengthOfIntegerOneShouldBeSequenceOfStringOneComma(self): 
        self.assertEquals('1,', self.getFizzBuzzSequenceOf(1) ) 

    def testFizzBuzzLengthOfIntegerTwoShouldBeSequenceOfStringOneCommaTwoComma(self): 
        self.assertEquals('1,2,', self.getFizzBuzzSequenceOf(2)) 
        
    def getFizzBuzzSequenceOf(self, length): 
        return FizzBuzz().sequenceOf(length) 

    



if __name__ == "__main__": 
    #import sys;sys.argv = ['', 'Test.testName'] 
    unittest.main() 