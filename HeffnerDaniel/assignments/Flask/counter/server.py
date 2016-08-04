from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SuperSecretNinjaKey"

@app.route('/')
def counter_setup():
	session['count'] = 0
	return redirect('/index')

@app.route('/index')
def index():
	session['count'] += 1
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	session['count'] +=1
	return redirect('/index')

@app.route('/hacker')
def hacker():
	session['count'] = 0
	return redirect('/index')

app.run(debug=True)