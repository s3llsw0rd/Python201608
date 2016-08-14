class Animal(object):
	def __init__(self, name, health = 100):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print self.name
		print self.health
		return self

animal = Animal('Animal')

animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health += 50
	def pet(self):
		self.health += 5
		return self

acheron = Dog('Acheron')

acheron.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health += 70
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print 'this is a dragon!'
		super(Dragon, self).displayHealth()

paarthunax = Dragon('Paarthunax')

paarthunax.walk().walk().walk().run().run().fly().fly().displayHealth()

# obviously, these don't work:
# animal.fly()
# animal.pet()