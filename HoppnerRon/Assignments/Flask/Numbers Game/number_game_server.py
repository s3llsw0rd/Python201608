from flask import Flask, render_template, redirect, session, request

import random

app = Flask(__name__)
app.secret_key = 'HatfieldsMama'

@app.route('/', methods = ['get', 'post'])
def number_game_index():

	status = {}

	try:
		session['num']
	except:
		session['num'] = random.randrange(0, 101)

	try:
		guess = int(request.form['guess'])
		if guess > session['number']:
			status = {'outcome':'Little Much'}
			status['coloration'] = 'red'
		elif guess < session['number']:
			status = {'outcome':'Getting Colder'}
			status['coloration'] = 'blue'
		else:
			status = {'outcome':'Spot On! Someone is pretty good at this!'}
			status['coloration'] = 'green'
			status['correct'] = 'true'
	except:
		status = {'outcome':'Pick a number. Come on, you know you want to...'}
		status['guess'] = 'Waiting for a guess...'
		status['coloration' : 'white']
		print status

	return render_template('number_game_index.html', status = status)

@app.route('/reset', methods = ['GET'])
def reset():
	session['num'] = random.randrange(0, 101)
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
