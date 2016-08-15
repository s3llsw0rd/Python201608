from time import strftime
from system.core.controller import *

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)

    def index(self):
        date = strftime('%b %d, %Y')
        time = strftime('%I:%M:%S %p')
        return self.load_view('index.html', date=date, time=time)

