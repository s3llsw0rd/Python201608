from flask import  Flask, render_template, request, redirect, session
import random, time
app= Flask(__name__)
app.secret_key ="very secret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []


    return render_template("index.html", gold=session['gold'], activities=reversed(session['activities']))

@app.route('/process_money' , methods=['POST'])
def process():
    place =request.form['place']
    if request.form['place'] =='farm':
        gold_amt = random.randint(10, 21)
        session['gold'] += gold_amt
        msg = "You earned " + str(gold_amt) + " golds from the farm!...." + time.strftime(" ( %Y/%m/%d     %I:%M %p )")
        messages ={
        'msg':msg,
        'color': 'green',
        }
        session['activities'].append(messages)
        # return redirect ("/")
    elif place =='cave':
        gold_amt = random.randint(5, 11)
        session['gold'] += gold_amt
        msg = "You earned " + str(gold_amt) + " golds from the cave!....." + time.strftime(" ( %Y/%m/%d     %I:%M %p )")
        messages ={
        'msg':msg,
        'color': 'green',
        }
        session['activities'].append(messages)

        # return redirect ("/")
    elif place =='house':
        gold_amt = random.randint(2, 6)
        session['gold'] += gold_amt
        msg = "You earned " + str(gold_amt) + " golds from the house!...." + time.strftime(" ( %Y/%m/%d  %I:%M %p )")
        messages ={
        'msg':msg,
        'color': 'green',
        }
        session['activities'].append(messages)
        # return redirect ("/")
    elif place =='casino':
        gold_amt = random.randint(-50, 51)
        session['gold'] += gold_amt
        if gold_amt > 0:
            msg = "You earned " + str(gold_amt) + " golds from the casino!..."  + time.strftime(" ( %Y/%m/%d     %I:%M %p )")
            messages ={
            'msg':msg,
            'color': 'green',
            }
            session['activities'].append(messages)
        elif gold_amt < 0:
            msg = "You lost " + str(gold_amt * -1) + " golds from the casino...  OUCH!..." + time.strftime("( %Y/%m/%d     %I:%M %p )")
            messages ={
            'msg':msg,
            'color': 'red',
            }
            session['activities'].append(messages)
    return redirect ("/")
app.run(debug=True)
