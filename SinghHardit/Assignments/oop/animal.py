class Animal(object):
	def __init__(self,name,health=100):
		self.name = name
		self.health = health
	
	def walk(self):
		if self.health > 0:
			self.health -= 1
		return self
	def run(self):
		if self.health > 5:
			self.health -= 5
		return self
	def display_health(self):
		print "Name: {}".format(self.name)
		print "Health: {}".format(self.health)
		return self

animal =Animal("animal")

animal.walk().walk().walk().run().run().display_health()

class Dog(Animal):
	def __init__(self,name,health=150):
		self.name = name
		self.health = health
	def pet(self):
		self.health += 5	
		return self

dog = Dog("fluffy")
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
	def __init__(self,name,health=170):
		self.name = name
		self.health = health
	def fly(self):
		if self.health > 10:
			self.health -= 10
		return self
	def display_health(self):
		print "This is a dragon"
		super(Dragon,self).display_health() 

dragon = Dragon("Draco")

dragon.walk().walk().walk().run().run().fly().fly().display_health()

	