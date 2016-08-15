from animal import Animal
from dragon import Dragon
from dog import Dog

print '\n'
animal = Animal('whooo')
animal.walk().walk().walk().run().run().displayHealth()
print '\n'
dog = Dog('fido')
dog.walk().walk().walk().run().run().pet().displayHealth()
print '\n'
dragon = Dragon('Draco')
dragon.walk().run().fly().displayHealth()
print '\n'
