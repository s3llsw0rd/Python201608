class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    #
    # def ride(self):
    #     pass
    #     return self

    def displayInfo(self):
        print 'The price is: $' + str(self.price)
        print 'The bikes max speed is: ' + str(self.max_speed) + 'mph'
        print 'The total miles ridden are: ' + str(self.miles)
        return self

    def drive(self):
        print 'Driving'
        self.miles += 10
        return self

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(87.99, 10)
bike1.drive().drive().drive().reverse().displayInfo();

bike2 = Bike(95.99, 15)
bike2.drive().drive().drive().reverse().displayInfo();
