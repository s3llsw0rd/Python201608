class Bike(object):
	def __init__(self,price,max_speed,miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print self.price,self.max_speed,self.miles
		return self
	def ride(self,times):
		print "Riding"
		self.miles+=10*times
		return self
	def reverse(self,times):
		print "Reversing"
		if not (self.miles -5*times) < 0:
			self.miles-=5*times
			return self
		else:
			return self	

bike1=Bike(200,"25mph")
bike2=Bike(300,"30mph")
bike3=Bike(150,"15mph")

bike1.ride(3).reverse(1).displayInfo()
bike2.ride(2).reverse(2).displayInfo()
bike3.reverse(3).displayInfo()

