class FibonacciGenerator(object):
	
	def getFibonacciNumberAtPosition(self, position):
		if position == 0 :		
			return 0
		elif position == 1:
			return 1
		else:
			return self.getFibonacciNumberAtPosition(position - 1) + self.getFibonacciNumberAtPosition(position - 2)

	def getFibonacciSequence(self, length):
		if length < 8 or length > 20:
			raise ValueError()
		
		fibonacciSequence = []
		for number in range(length):
			fibonacciSequence.append(self.getFibonacciNumberAtPosition(number))
		
		return fibonacciSequence		


	def fib(self, n): # return Fibonacci series up to n
		"Return a list containing the Fibonacci series up to n"
		result = []
		a, b = 0, 1

		while b < n:
			result.append(b)    # see below
			a, b = b, a + b
		
		return result



