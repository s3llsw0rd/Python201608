from flask import Flask, render_template, redirect, request, session, flash
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NUMBER = re.compile('[0-9]')
NON_ALPHANUMERIC = re.compile('\W')
CAPITAL = re.compile('[A-Z]')
BDAY = re.compile('^(\d\d\d\d)-(\d\d)-(\d\d)$')

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess'

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	error = False
	if len(request.form['email']) < 1:
		flash('email cannot be blank', 'email')
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address', 'email')
		error = True
	
	if len(request.form['fname']) < 1:
		flash('first name cannot be blank', 'fname')
		error = True
	if NUMBER.search(request.form['fname']) or NON_ALPHANUMERIC.search(request.form['fname']):
		flash('First name contains illegal characters', 'fname')
		error = True

	if len(request.form['lname']) < 1:
		flash('last name cannot be blank', 'lname')
		error = True
	if NUMBER.search(request.form['lname']) or NON_ALPHANUMERIC.search(request.form['lname']):
		flash('last name contains illegal characters', 'lname')
		error = True

	if len(request.form['bday']) < 1:
		flash('birthday cannot be blank', 'bday')
		error = True
	if not BDAY.match(request.form['bday']):
		flash('must be a valid date formatted correctly', 'bday')
		error = True
	else:
		bd = BDAY.match(request.form['bday'])
		y,m,d = bd.groups()
		now = datetime.datetime.now()
		if int(y) > now.year:
			flash('you were not born in the future', 'bday')
			error = True
		if int(m) > 12:
			flash('not a valid month', 'bday')
			error = True
		if int(d) > 31:
			flash('no month has more than 31 days', 'bday')
			error = True

	if len(request.form['password']) < 8:
		flash('password must be 8 characters or more', 'pw')
		error = True
	if not NUMBER.search(request.form['password']) or not CAPITAL.search(request.form['password']):
		flash('password must have at least one number and one capital letter', 'pw')
		error = True

	if len(request.form['pwconfirm']) < 1:
		flash('type your password again here to confirm it', 'pwconfirm')
		error = True
	elif request.form['password'] != request.form['pwconfirm']:
		flash("that's not the same password", 'pwconfirm')
		error = True

	if not error:
		flash('thanks for submitting your information', 'success')
	return redirect('/')

app.run(debug=True)