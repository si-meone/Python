class FizzBuzzGame(object):
    
    def getFizzBuzzNumber(self, number):
        
        result = ""
        
        if number % 3 == 0 :
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        
        if result != "":
            return result;
        
        return str(number)
    
    def getFizzBuzzSequence(self, length):
        sequence = ""
        for number in range(1, length + 1):
            sequence += (self.getFizzBuzzNumber(number) + ',')
        return sequence[0:-1]