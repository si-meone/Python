'''
Created on 11 Jan 2010

@author: nasras01
'''
import unittest
from RomanNumerals import toNumerals, fromNumerals

class TestToNumerals(unittest.TestCase):

    def testOneIsNumeralI(self):
        self.assertEquals(toNumerals(1), 'I')
        
    def testTwoIsNumeralII(self):
        self.assertEqual(toNumerals(2), 'II')
    
    def testFourIsNumeralIV(self):
        self.assertEqual(toNumerals(4), 'IV')
    
    def testFiveIsNumeralV(self):
        self.assertEquals(toNumerals(5), 'V')

    def testSixIsNumeralVI(self):
        self.assertEquals(toNumerals(6), 'VI')

    def testEightIsNumeralVIII(self):
        self.assertEquals(toNumerals(8), 'VIII')
        
    def testNineIsNumeralIX(self):
        self.assertEquals(toNumerals(9), 'IX')
    
    def testTenIsNumeralX(self):
        self.assertEquals(toNumerals(10), 'X')

    def testFourteenIsNumeralXIV(self):
        self.assertEquals(toNumerals(14), 'XIV')

    def testFourtyIsNumeralXL(self):
        self.assertEquals(toNumerals(40), 'XL')

    def testFiftyIsNumeralL(self):
        self.assertEquals(toNumerals(50), 'L')

    def testNinetyIsNumeralXC(self):
        self.assertEquals(toNumerals(90), 'XC')

    def testOneHundredIsNumeralC(self):
        self.assertEquals(toNumerals(100), 'C')

    def testFourHundredIsNumeralCD(self):
        self.assertEquals(toNumerals(400), 'CD')

    def testFiveHundredIsNumeralD(self):
        self.assertEquals(toNumerals(500), 'D')

    def testTheNumberOfTheBeastIsNumeralDCLXVI(self):
        self.assertEquals(toNumerals(666), 'DCLXVI')

    def testNineHundredIsNumeralCM(self):
        self.assertEquals(toNumerals(900), 'CM')
    
    def testOneThousandIsNumeralM(self):
        self.assertEquals(toNumerals(1000), 'M')
        
    def testThreeThousandNinentyNineIsNumeralMMMCMXCIX(self):
        self.assertEquals(toNumerals(3999), 'MMMCMXCIX')
        
    def testTooLowOutOfBoundsNumberRaisesException(self):
        self.assertRaises(ValueError, toNumerals, 0)
        
    def testTooHighOutOfBoundsNumberRaisesException(self):
        self.assertRaises(ValueError, toNumerals, 4000)

class TestFromNumerals(unittest.TestCase):

    def testNumeralIisOne(self):
        self.assertEquals(fromNumerals('I'), 1)

    def testNumeralIIisTwo(self):
        self.assertEquals(fromNumerals('II'), 2)

    def testInvalidNumeralRaisesException(self):
        self.assertRaises(ValueError, fromNumerals, 'Z')

    def testNumeralIVisFour(self):
        self.assertEquals(fromNumerals('IV'), 4)                               

    def testNumeralDCLXVIisTheNumberOfTheBeast(self):
        self.assertEquals(fromNumerals('DCLXVI'), 666)

    def testInvalidNumeralSequenceRaisesException(self):
        self.assertRaises(ValueError, fromNumerals, 'VX')

    def testNumeralMMMCMXCIXisThreeThousandNinentyNine(self):
        self.assertEquals(fromNumerals('MMMCMXCIX'), 3999)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

