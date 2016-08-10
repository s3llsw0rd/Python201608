from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = "lahfog3sl"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if request.form['action'] == 'add_email':
		if len(request.form['email']) < 1:
			flash("you didn't submit anything", 'email')
			error = True
		elif not EMAIL_REGEX.match(request.form['email']):
			flash("that's not a valid email address", 'email')
			error = True
		else:
			query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
			data = { 'email': request.form['email'] }
			mysql.query_db(query, data)
			flash("the email address you entered (" + request.form['email'] + ") is a valid email address. Thank you!", 'success')
			return redirect('/success')
	elif request.form['action'] == 'delete':
		query = 'DELETE FROM emails WHERE email = :email'
		data = {'email': request.form['email']}
		mysql.query_db(query, data)
		return redirect('/success')
	else:
		return redirect('https://www.youtube.com/watch?v=GFLGRidfFo4')
	#also put n an if statement and the code to delete an email address
	return redirect('/')

@app.route('/success')
def success():
	query = "SELECT email, created_at FROM emails"
	email_addresses = mysql.query_db(query)
	return render_template('success.html', email_addresses=email_addresses)

app.run(debug=True)