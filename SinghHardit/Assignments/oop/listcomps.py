

class Other(object):
    def override(self):
        print "OTHER override()"
    def implicit(self):
        print "OTHER implicit()"
    def altered(self):
        print "OTHER altered()"

# notice how the Child class does not inherit from the Other class
# however there may be some cases where we want to use some attributes/methods
# from the Other class
class Child(object):
    def __init__(self):
        self.other = Other()
    
 
son = Child()
son.other.implicit()
