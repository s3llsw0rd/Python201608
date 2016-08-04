from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__) 
app.secret_key = "VerySecretTellNoOne"

@app.route('/')
def index():
	try:
		session['number']
	except:
		session['number'] = random.randrange(0, 101)
	try:
		session['response']
	except:
		session['response'] = ''

	return render_template('index.html')
	
@app.route('/process', methods=['POST'])
def process():
	session['guess'] = int(request.form['guess'])
	if session['guess'] == session['number']:
		session['response'] = str(session['guess']) + ' was the number!'
	elif session['guess'] < session['number']:
		session['response'] = "Too low!"
	elif session['guess'] > session['number']:
		session['response'] = "Too high!"
	return redirect('/')

@app.route('/refresh')
def refresh():
	session.pop('number')
	session.pop('response')
	session.pop('guess')
	return redirect('/')

app.run(debug=True)