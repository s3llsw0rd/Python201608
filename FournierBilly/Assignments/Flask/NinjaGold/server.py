from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template("index.html", gold=session['gold'])


import time
from datetime import datetime
@app.route('/process_money', methods=['POST'])
def process_money():
    i = datetime.now()
    date = i.strftime('%Y/%m/%d %I:%M %p')
    buildings = {
        'farm':random.randint(5,10),
        'cave':random.randint(0,30),
        'house':random.randint(0,5),
        'casino':random.randint(-50,50)
    }
    if request.form['building'] in buildings:
        """ OMG What???"""
        result = buildings[request.form['building']]
        session['gold'] = session['gold']+result
        result_dictionary = {
                                'class': ('red','green')[result > 0],
                                'activity': "You went to the {} and {} {} gold!".format(request.form['building'],
                                    ('lost','gained')[result > 0], result)
                            }
        session['activity'].append(result_dictionary)
    return redirect('/')

app.run(debug=True) # run our servers
