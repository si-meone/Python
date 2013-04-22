class FibonacciGenerator(object):
	
	def getFibonacciNumberAtPosition(self, n):
		fib = lambda n: fib(n-1) + fib(n-2) if n > 1 else n
		return fib(n)
	
	def getFibonacciSequence(self, length):
		pass

if __name__ == '__main__':
	print 'here'
	print FibonacciGenerator().getFibonacciNumberAtPosition(7)

