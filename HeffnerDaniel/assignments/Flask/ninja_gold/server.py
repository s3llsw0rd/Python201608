from flask import Flask, render_template, request, redirect, session
import datetime
import random

app=Flask(__name__)
app.secret_key='NinjaMoneyGameYo'

@app.route('/')
def index():
	try:
		session['yourgold']
	except:
		session['yourgold'] = 0
	try:
		session['activities']
	except:
		session['activities'] = []

	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['action'] == 'farm':
		earn = random.randrange(10, 21)
		session['yourgold'] += earn
		session['activities'].append({'color': 'green', 'alert': 'Earned ' + str(earn) + ' gold from the farm! ' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p') + '\n'})
		return redirect('/')
	elif request.form['action'] == 'cave':
		earn = random.randrange(5, 11)
		session['yourgold'] += earn
		session['activities'].append({'color': 'green', 'alert': 'Earned ' + str(earn) + ' gold from the cave! ' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p') + '\n'})
		return redirect('/')
	elif request.form['action'] == 'house':
		earn = random.randrange(2, 6)
		session['yourgold'] += earn
		session['activities'].append({'color': 'green', 'alert': 'Earned ' + str(earn) + ' gold from the house! ' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p') + '\n'})
		return redirect('/')
	elif request.form['action'] == 'casino':
		earn = random.randrange(-50, 51)
		session['yourgold'] += earn
		if earn >= 0:
			session['activities'].append({'color': 'green', 'alert': 'Earned ' + str(earn) + ' gold from the casino! ' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p') + '\n'})
		else:
			session['activities'].append({'color': 'red', 'alert': 'Entered the casino and lost ' + str(earn) + ' gold... Ouch.' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p') + '\n'})
		return redirect('/')

@app.route('/reset')
def reset():
	session.pop('yourgold')
	session.pop('activities')
	return redirect('/')

app.run(debug=True)