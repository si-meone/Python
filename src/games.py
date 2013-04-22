class FizzBuzzWizzGenerator(object):
			
	def __call__(self, num):
		try:
			int(num)
			if	self.is_divisable_by_3(num) and self.is_divisable_by_5(num):
				return 'wizz'
			elif self.is_divisable_by_3(num):
				return 'fizz'
			elif self.is_divisable_by_5(num):
				return 'buzz'
			else:
				return num
		except ValueError:
			raise ValueError
	
	def is_divisable_by_3(self, num):
		return num % 3 == 0

	def is_divisable_by_5(self, num):
		return num % 5 == 0