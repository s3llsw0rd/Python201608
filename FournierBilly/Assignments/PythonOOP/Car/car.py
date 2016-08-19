class car(object):
    def __init__(self,price=1000, speed=75, fuel='Full', mileage=20):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def displayAll(self):
        print 'Price: ', self.price
        print 'Speed: ', self.speed,'mph'
        print 'Fuel:', self.fuel
        print 'Milage: ', self.mileage,'mpg'
        print 'Tax: ', self.tax, '\n'

c1 =car(2000,35,'Full',15)
c1.displayAll()

c2 =car(2000,5,'Not Full',105)
c2.displayAll()

c3 =car(2000,15,'Kind of Full',95)
c3.displayAll()

c4 =car(2000,25,'Full',25)
c4.displayAll()

c5 =car(2000,45,'Empty',25)
c5.displayAll()

c6 =car(2000000,35,'Empty',15)
c6.displayAll()
