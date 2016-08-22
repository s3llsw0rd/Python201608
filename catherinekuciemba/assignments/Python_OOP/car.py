class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    def taxes(self):
        if (self.price >10000):
            self.tax = .15
        else:
            self.tax = .12
    def displayInfo(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage)
        print 'Tax: ' + str(self.tax)


car1 = Car(10000, 200, 'empty', 35)
car1.taxes()
car1.displayInfo()
