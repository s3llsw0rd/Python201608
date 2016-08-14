class MathDojo(object):
	def __init__(self, result = 0):
		self.result = result
	def add(self, x, *y):
		self.result += x
		for num in y:
			self.result += num
		return self
	def subtract(self, x, *y):
		self.result -= x
		for num in y:
			self.result -= num
		return self


md = MathDojo()
print md.add(2).add(2, 5).subtract(3,2).result