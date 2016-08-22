class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100


    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'The name of the animal is ' + str(self.name)
        print 'The animals health is ' + str(self.health)
        return self

# from Animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health=150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.heath=170

    def fly(self):
        self.health -=10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()


animal1 = Animal('animal')
animal1.walk().walk().walk().run().run().displayHealth();

dog1=Dog('dog')
dog1.walk().walk().walk().run().run().pet().displayHealth();

dragon1=Dragon('dragon')
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth();
