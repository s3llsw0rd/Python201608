class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'The price is: $' + str(self.price)
        print 'The bikes max speed is: ' + str(self.max_speed) + 'mph'
        print 'The total miles ridden are: ' + str(self.miles) 

    def drive(self):
        print 'Driving'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(87.99, 10)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(95.99, 15)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
