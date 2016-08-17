from system.core.controller import *
from flask import Markup
import random

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        if "gold" not in session:
            session["gold"] =  0
            session['activities']=""        
        return self.load_view('index.html')
    
    def processMoney(self):
        if request.form['place'] == "farm":
            gold = random.randint(10,20)        
            session['gold']+=gold
            session['activities']+=Markup("<p>earned {} gold from the farm</p>".format(gold))
            return redirect("/")
        elif request.form['place'] == "cave":
            gold = random.randint(5,10)
            session['gold']+=gold
            session['activities']+=Markup("<p>earned {} gold from the cave</p>".format(gold))
            return redirect("/")
        elif request.form['place'] == "house":
            gold = random.randint(2,5)
            session['gold']+=gold
            session['activities']+=Markup("<p>earned {} gold from the house</p>".format(gold))
            return redirect("/")
        elif request.form['place'] == "casino":
            gold = random.randint(-50,50)
            session['gold']+=gold
            if gold > 0:
                session['activities']+=Markup("<p>entered a casino and made {} gold</p>".format(gold))
            else:
                session['activities']+=Markup("<p class= 'red'>entered a casino and lost {} gold..Ouch</p>".format(gold*-1))
            return redirect("/")
                

