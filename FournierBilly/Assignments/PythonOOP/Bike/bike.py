class bike(object):
    def __init__(self,price=200,max_spd=25, miles=0):
        self.price = price
        self.max_spd= max_spd
        self.miles = miles
    def displayInfo(self):
        print '----------------------'
        print '| Price is: ',self.price
        print '| Max speed is: ', self.max_spd
        print '| Miles ridden is: ', self.miles
        print '----------------------'
    def ride(self):
        print 'Riding'
        self.miles += 10
    def reverse(self):
        print "Reversing"
        self.miles -= 5

b1 = bike()
b2 = bike()
b3 = bike()
for i in range(3):
    b1.ride()
b1.reverse()
b1.displayInfo()
for i in range(2):
    b2.ride()
for i in range(2):
    b2.reverse()
b2.displayInfo()
for i in range(3):
    b3.reverse()
b3.displayInfo()
