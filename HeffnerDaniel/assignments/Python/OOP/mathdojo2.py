class MathDojo(object):
	def __init__(self, result = 0):
		self.result = result
	def add(self, x, *y):
		if type(x) == list:
			for num in x:
				self.result += num
		else:
			self.result += x
		for num in y:
			if type(num) == list:
				for ber in num:
					self.result += ber
			else:
				self.result += num
		return self
	def subtract(self, x, *y):
		if type(x) == list:
			for num in x:
				self.result -= num
		else:
			self.result -= x
		for num in y:
			if type(num) == list:
				for ber in num:
					self.result -= ber
			else:
				self.result -= num
		return self

md = MathDojo()

print md.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2, [2,3],[1.1,2.3]).result