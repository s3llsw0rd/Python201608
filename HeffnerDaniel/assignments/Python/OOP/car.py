import random

class Car(object):
	def __init__(self, price = 10000, speed = 70, fuel = 15, mileage = 0):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print '------------------'
		print 'Price: ' + str(self.price)
		print 'Speed: ' + str(self.speed)
		print 'Fuel: ' + str(self.fuel)
		print 'Mileage: ' + str(self.mileage)
		print 'Tax: ' + str(self.tax)

c1 = Car(random.randrange(5000,30000), random.randrange(50,150), random.randrange(10,50), random.randrange(0,3000))
c2 = Car(random.randrange(5000,30000), random.randrange(50,150), random.randrange(10,50), random.randrange(0,3000))
c3 = Car(random.randrange(5000,30000), random.randrange(50,150), random.randrange(10,50), random.randrange(0,3000))
c4 = Car(random.randrange(5000,30000), random.randrange(50,150), random.randrange(10,50), random.randrange(0,3000))
c5 = Car(random.randrange(5000,30000), random.randrange(50,150), random.randrange(10,50), random.randrange(0,3000))
c6 = Car(random.randrange(5000,30000), random.randrange(50,150), random.randrange(10,50), random.randrange(0,3000))
