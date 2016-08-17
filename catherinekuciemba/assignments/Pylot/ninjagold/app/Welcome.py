"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
import random
from time import strftime
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):

        if 'gold' not in session:
            session['gold'] = 0
        if 'activities' not in session:
            session['activities'] = []
        return self.load_view('index.html')

        # , gold=session['gold'], activities=reversed(session['activities']

    def process_money(self):
        building=request.form['building']
        if request.form['building'] =='farm':
            gold = random.randint(10, 21)
            session['gold'] += gold
            msg = "You earned " + str(gold) + " golds from the farm!...." + strftime(" ( %Y/%m/%d %I:%M %p )")
            messages ={
            'msg':msg,
            'color': 'green',
            }
            session['activities'].append(messages)
        elif building =='cave':
            gold = random.randint(5, 11)
            session['gold'] += gold
            msg = "You earned " + str(gold) + " golds from the cave!....." + strftime(" ( %Y/%m/%d  %I:%M %p )")
            messages ={
            'msg':msg,
            'color': 'green',
            }
            session['activities'].append(messages)
        elif building =='house':
            gold = random.randint(2, 6)
            session['gold'] += gold
            msg = "You earned " + str(gold) + " golds from the house!...." + strftime(" ( %Y/%m/%d %I:%M %p )")
            messages ={
            'msg':msg,
            'color': 'green',
            }
            session['activities'].append(messages)
        elif building =='casino':
            gold = random.randint(-50, 51)
            session['gold'] += gold
            if gold > 0:
                msg = "You earned " + str(gold) + " golds from the casino!..."  + strftime(" ( %Y/%m/%d %I:%M %p )")
                messages ={
                'msg':msg,
                'color': 'green',
                }
                session['activities'].append(messages)
            elif gold < 0:
                msg = "You lost " + str(gold * -1) + " golds from the casino...  OUCH!..." + strftime("( %Y/%m/%d %I:%M %p )")
                messages ={
                'msg':msg,
                'color': 'red',
                }
                session['activities'].append(messages)
                print session['activities']

        return self.load_view('index.html', message=reversed(session['activities']))
