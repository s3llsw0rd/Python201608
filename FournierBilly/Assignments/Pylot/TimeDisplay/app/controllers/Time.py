from time import strftime
from system.core.controller import *

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db


    def index(self):
        date = strftime('%b %m %Y')
        time = strftime('%I:%M %p')
        return self.load_view('index.html', date=date, time=time)
