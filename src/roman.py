import re 
class RomanNumerals(): 
    def __init__(self): 
        self.ones = {1 : 'I', 
            2 : 'II', 
            3 : 'III', 
            4 : 'IV', 
            5 : 'V', 
            6 : 'VI', 
            7 : 'VII', 
            8 : 'VIII', 
            9 : 'IX', 
            } 
        
        self.tens = {1 : 'X', 
            2 : 'XX', 
            3 : 'XXX', 
            4 : 'XL', 
            5 : 'L', 
            6 : 'LX', 
            7 : 'LXX', 
            8 : 'LXXX', 
            9 : 'XC', 
            } 
        self.hundreds = {1 : 'C', 
            2 : 'CC', 
            3 : 'CCC', 
            4 : 'CD', 
            5 : 'D', 
            6 : 'DC', 
            7 : 'DCC', 
            8 : 'DCCC', 
            9 : 'CM', 
            } 
        self.thousands = {1 : 'M', 
            2 : 'MM', 
            3 : 'MMM', 
            } 
    
        self.romanNum = '' 
        self.number = 0 
    def toRoman(self, num): 
        if num < 1 or num > 3999: 
            raise ValueError("invalid numeral range") 
        if num > 0 and num < 10: 
            self.romanNum += self.ones[num] 
        elif num > 9 and num < 100 : 
            self.toRomanHelper(num, self.tens, 10) 
        elif num > 99 and num < 1000 : 
            self.toRomanHelper(num, self.hundreds, 100) 
        elif num > 999 and num < 10000 : 
            self.toRomanHelper(num, self.thousands, 1000) 
        return self.romanNum 
    
    
    def toRomanHelper(self, num,  lookupTable, divisable): 
        self.romanNum += lookupTable[num / divisable] 
        print 'self.romanNum = ', self.romanNum 
        num = num % divisable 
        print 'num = ' , num 
        if num != 0: #if you have stuff left 
                self.toRoman(num) 
    
    def fromRoman(self, numeral): 
        romanNumeralPattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$' 
        if not re.search(romanNumeralPattern, numeral): 
            raise ValueError("Invalid numeral: " + numeral) 
        
        if numeral[0] == 'I' or numeral[0] == 'V': 
            for k, v in self.ones.items(): 
                if numeral == v: 
                    self.number += k 
        elif numeral[0] == 'X' or numeral[0] == 'L': 
            self.fromRomanHelper(numeral, self.tens, 10) 
        elif numeral[0] == 'C' or numeral[0] == 'D': 
            self.fromRomanHelper(numeral, self.hundreds, 100) 
        elif numeral[0] == 'M': 
            self.fromRomanHelper(numeral, self.thousands, 1000) 
            
        return self.number 
    
    def fromRomanHelper(self, numeral,  lookupTable, divisable): 
        highest = 0 
        for k, v in lookupTable.items(): 
            if v in numeral: 
                if k > highest: 
                    highest = k 
        self.number += (int(highest) * divisable) 
        numeral = numeral.replace(lookupTable[highest], '', 1) 
        if numeral != '': 
            self.fromRoman(numeral) 
if __name__ == '__main__': 
    #fromRoman 
    print ("toRoman") 
    print(RomanNumerals().toRoman(742))
#    print(RomanNumerals().toRoman(1)) 
#    print(RomanNumerals().toRoman(9)) 
#    print(RomanNumerals().toRoman(10)) 
#    print(RomanNumerals().toRoman(11)) 
#    print(RomanNumerals().toRoman(99)) 
#    print(RomanNumerals().toRoman(100)) 
#    print(RomanNumerals().toRoman(505)) 
#    print(RomanNumerals().toRoman(999)) 
#    print(RomanNumerals().toRoman(1000)) 
#    print(RomanNumerals().toRoman(3999)) 
#    print(RomanNumerals().toRoman(3888)) 
#    
#    #fromRoman 
#    print ("\nfromRoman") 
#    print(RomanNumerals().fromRoman('I'))#1 
#    print(RomanNumerals().fromRoman('IX'))#9 
#    print(RomanNumerals().fromRoman('X'))#10 
#    print(RomanNumerals().fromRoman('XI'))#11 
#    print(RomanNumerals().fromRoman('XCIX')) #99 
#    print(RomanNumerals().fromRoman('DCLXVI')) #666 
#    print(RomanNumerals().fromRoman('MMMDCCCLXXXVIII')) #3888 
