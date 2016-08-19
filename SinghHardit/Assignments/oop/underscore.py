class Underscore(object):
    def map(self,*args):
		try:
			return [args[1](i) for i in args[0]]
		except:
			return "invalid inputs"			        
    def reduce(self,*args):
				count = 0
				try:
					for i in args[0]:
						if count == 0:
							reduced = args[0][0]
						else:
							reduced = args[1](reduced,i)
						count+=1	
					return reduced
				except:
					return "invalid input"			
    def find(self,*args):
		try:
			for i in args[0]:
				if args[1](i):
					return i
		except:
			return "no match found"
    def filter(self,*args):		
		try:
			return [i for i in args[0] if args[1](i)]
		except:
			return "invalid inputs" 
    def reject(self,*args):
		try:
			return [i for i in args[0] if not args[1](i)]
		except:
			return "invalid inputs" 
_ = Underscore() 
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
squares = _.map([1, 2, 3, 4, 5, 6], lambda x: x ** 2)
red = _.map({1: 2, 3: 4, 5: 6}, lambda x: x*2)
print red
# should return [2, 4, 6] after you finish implementing the code above