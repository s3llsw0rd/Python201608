class Underscore(object):
	def map(self, lst, lam):
		# maps each value in a list through a transformation function. for example: [1,2,3] with a function that returns num*3 would give you [3,6,9]
		arr = []
		for val in lst:
			arr.append(lam(val))
		return arr
	def reduce(self, lst, lam, mem = False):
		# takes a list and a function(memo, context) and uses the function to boil down the list into one value. memo is the initial state for the reduction function, if no memo is passed, the first value in the list takes its place
		if not mem:
			mem = lst[0]
			lst.pop(0)
		for ele in lst:
			mem = lam(mem, ele)
		return mem
	def find(self, lst, lam):
		# looks through each value in a list, returning the first that passes a truth test that is one of the arguments in calling this function
		for ele in lst:
			if lam(ele) == True:
				return ele
		return False
	def filter(self, lst, lam):
		# same as find, but returns all that pass the test instead of just the first
		arr = []
		for ele in lst:
			if lam(ele) == True:
				arr.append(ele)
		return arr
	def reject(self, lst, lam):
		# opposite of filter, return all values from a list that do not pass a truth test.
		arr = []
		for ele in lst:
			if lam(ele) == False:
				arr.append(ele)
		return arr

_ = Underscore()

print '_.map test:'
print _.map([1,2,3,4,5], lambda x: x % 3)

print  '_.reduce tests:'
print _.reduce([5,6,7,8,9], (lambda mem, x: mem * x))
print _.reduce([5,6,7,8,9], (lambda mem, x: mem * x), 3)

print '_.find test:'
print _.find([5342,123,456,542], lambda x: x % 3 == 0)

print '_.filter test:'
print _.filter([5342,123,456,542], lambda x: x % 3 == 0)

print '_.reject test:'
print _.reject([5342,123,456,542], lambda x: x % 3 == 0)