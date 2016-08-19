def flatten(*args):
	flat = []	
	def check(l):	
		for i in l:			
			if isinstance(i, (int,float)):
				flat.append(i)	
			else:
				check(i)			
	check(args)			
	return flat		

class MathDojo(object):
	def __init__(self,result = 0.0):
		self.result = result
	def add(self,*args):
		self.result+= sum(flatten(args))
		return self
	def subtract(self,*args):
		sub_sum = sum(flatten(args))
		self.result-=sub_sum
		return self

md = MathDojo()
print MathDojo().add([1],3,4).add([3, 5,[], 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result


# def disp(self,*args):
# 		# x = [j if isinstance(i, (list,tuple)) else i for i in args for j in i]
# 		x = [i for i in args if isinstance(i, (int)) ]
# 		y = [j for i in args if isinstance(i, (list,tuple)) for j in i ]
# 		print x + y