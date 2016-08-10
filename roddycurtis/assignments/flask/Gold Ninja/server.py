from flask import Flask, render_template, request, redirect, session
import datetime
import random

app=Flask(__name__)
app.secret_key='ninjagame'

@app.route('/')
def index():
     if 'gold' not in session:
		session['gold']= 0
	 # if 'activities' not in session:
		# session['activities']=[]
     return render_template('index.html',gold=session['gold'], activities=session[activities])

@app.route('/process_money', methods=["post"])
def process_money():
	location= request.form["location"]

	if location=="farm":
		gold_change=random.randint(10, 20)
		session['gold']+=gold_change
		session['activities'].append({'Earned'+gold_change+'gold from the farm!'})
		return redirect ('/')
	elif location=="Cave":
		gold_change=random.randint(10, 20)
		session['gold']+=gold_change
		return redirect ('/')
	elif location=="House":
		gold_change=random.randint(10, 20)
		session['gold']+=gold_change
		return redirect ('/')
	elif location=="Casino":
		gold_change=random.randint(10, 20)
		session['gold']+=gold_change
	return redirect('/')
app.run(debug=True)