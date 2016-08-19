class Bike(object):
	def __init__(self, price=100, max_speed='25mph'):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'price: ' + str(self.price)
		print 'max speed: ' + self.max_speed
		print 'total miles: ' + str(self.miles)
		return self
	def ride(self):
		print 'they see me riding...'
		self.miles += 10
		return self
	def reverse(self):
		print 'reverse reverse reverse'
		self.miles -= 5
		return self

schwinn = Bike(75, '10mph')
trek = Bike(1125, '40mph')
giant = Bike(500, '30mph')

print '---------------------'
print 'Schwinn:'
schwinn.ride().ride().ride().reverse().displayInfo()
print '---------------------'
print 'Trek:'
trek.ride().ride().reverse().reverse().displayInfo()
print '---------------------'
print 'Giant:'
giant.reverse().reverse().reverse().displayInfo()
print '---------------------'
"""
In answer to the assignment's question 'What would you do to prevent the instance from having negative miles?', I would like to submit that the simplest way to do that would be to mirror the real world and count miles traveled in reverse as ADDING miles to the total mileage, not subtracting them in some sort of Sgt. Bilko-esque exercise in absurdity. Barring bowing to the constraints of the physical world, we could add an if statement to the reverse() method, and if the miles is 0, we could print that the user has to ride forward more before reversing any further.
"""