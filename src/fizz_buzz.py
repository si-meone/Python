''' 
Created on 17 May 2010 

@author: nasras01 
''' 


class FizzBuzz(object): 
    ''' 
    classdocs 
    ''' 



    def __init__(self): 
        ''' 
        Constructor 
        ''' 

    def valueOf(self, number): 
        result = '' 
        
        if self.isDivisableByThree(number): 
            result += 'fizz' 
        if self.isDivisableByFive(number): 
            result += 'buzz' 
        
        if result != '': 
            return result 
         
        return str(number) 
    
    def isDivisableByThree(self, number): 
        return number % 3 == 0 

    def isDivisableByFive(self, number): 
        return number % 5 == 0 

    def sequenceOf(self, length): 
        sequence = '' 
        for number in range(1, length + 1): 
            sequence += self.valueOf(number) + ',' 
        
        return sequence