from flask import Flask, render_template,redirect,session, flash,request
import re

from  datetime import datetime 

app = Flask(__name__)
app.secret_key = "secretKey"

name_regex = re.compile(r'[0-9]')
pass_regex = re.compile(r'[A-Z0-9]')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/reg", methods=['POST'])
def registration():
	session['formValues'] = {
		'Email':request.form['email'],
		'First name': request.form['first_name'],
		'Last name': request.form['last_name'],
		'Password': request.form['password'],
		'Confirm password': request.form['confirm'],
		'Birth Date': str(request.form['birthDate'])
	}
	tday = datetime.today()
	bday =	datetime.strptime(session['formValues']['Birth Date'],'%Y-%m-%d')	

	for i in session['formValues']:
		if len(session['formValues'][i]) <1:
			flash('{0} cannot be empty'.format(i))

	if name_regex.match(session['formValues']['First name']):
		flash("First name cannot have a number")
	if name_regex.match(session['formValues']['Last name']):
		flash("Last name cannot have a number")	
	if len(session['formValues']['Password'])<9:
		flash("Password must be at least 9 characters")
	if not pass_regex.match(session['formValues']['Password']):
		flash("Password must have at least 1 number and one upper case character")	
	if session['formValues']['Confirm password'] != session['formValues']['Password']:
		flash("Confirm password must match password")	
	if  bday >= tday:		
		flash('Birth Date needs to be in the past')

	return redirect("/")
app.run(debug=True)
