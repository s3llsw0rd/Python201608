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
        return self
    def ride(self):
        print 'Riding'
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

b1 = bike()
b1.ride().ride().ride().reverse().displayInfo()
