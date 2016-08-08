from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'the_wall')
app.secret_key = "thewallofninjasecrets"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')

@app.route('/')
def index():
	# If logged on, log off
	if 'user_id' in session:
		session.pop('user_id')
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	# Login Validation
	error = False
	if request.form['action'] == 'login':
		# Email
		if len(request.form['login_email']) < 1:
			flash("you forgot to enter an email", 'login_email')
			error = True
		elif not EMAIL_REGEX.match(request.form['login_email']):
			flash("that's not a real email address", 'login_email')
			error = True
		else:
			query = 'SELECT email FROM users WHERE email = :email'
			data = { 'email': request.form['login_email'] }
			email = mysql.query_db(query, data)
			if request.form['login_email'].lower() != email[0]['email'].lower():
				flash("that email doesn't match any user", 'login_email')
				error = True
		# Password
		if len(request.form['login_password']) < 1:
			flash("you can't log in if you leave this blank", 'login_password')
			error = True
		elif len(request.form['login_password']) < 8:
			flash("passwords must be at least eight characters long", 'login_password')
			error = True

	# Registration Validation
	elif request.form['action'] == 'register':
		# First Name
		if len(request.form['reg_fname']) < 2:
			flash("sorry, your name must be more than one character long", 'reg_fname')
			error = True
		elif not LETTERS_ONLY.match(request.form['reg_fname']):
			flash("your name can only have letters in it", 'reg_fname')
			error = True
		# Last Name
		if len(request.form['reg_lname']) < 2:
			flash("sorry, your name must be more than one character long", 'reg_lname')
			error = True
		elif not LETTERS_ONLY.match(request.form['reg_lname']):
			flash("your name can only have letters in it", 'reg_lname')
			error = True
		# Email
		if len(request.form['reg_email']) < 1:
			flash("you forgot to enter an email", 'reg_email')
			error = True
		elif not EMAIL_REGEX.match(request.form['reg_email']):
			flash("that's not a real email address", 'reg_email')
			error = True
		else:
			query = 'SELECT email FROM users WHERE email = :email'
			data = { 'email': request.form['reg_email'] }
			check = mysql.query_db(query, data)
			if not check:
				pass
			elif request.form['reg_email'].lower() == check[0]['email'].lower():
				flash("that email is already in use", 'reg_email')
				error = True
		# Password
		if len(request.form['reg_password']) < 1:
			flash("you can't register without a password", 'reg_password')
			error = True
		elif len(request.form['reg_password']) < 8:
			flash("passwords must be at least eight characters long", 'reg_password')
			error = True
		# Confirm Password
		if not request.form['reg_password_confirm'] == request.form['reg_password']:
			flash("those passwords don't match", 'reg_password_confirm')
			error = True
	else:
		return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
	
	if error:
		return redirect('/')
	else:
		if request.form['action'] == 'login':
			query = "SELECT password FROM users WHERE email = :email"
			data = { 
				'email': request.form['login_email']
			}
			stored_pw = mysql.query_db(query, data)
			if not  bcrypt.check_password_hash(stored_pw[0]['password'], request.form['login_password']):
				flash("that wasn't the right password", 'login_password')
				return redirect('/')
			else:
				query = "SELECT id FROM users WHERE email = :email"
				data = {
					"email": request.form['login_email']
				}
				user_id = mysql.query_db(query, data)
				session['user_id'] = user_id[0]['id']
				return redirect("/wall")
		elif request.form['action'] == 'register':
			query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
			data = {
				'first_name': request.form['reg_fname'],
				'last_name': request.form['reg_lname'],
				'email': request.form['reg_email'],
				'password': bcrypt.generate_password_hash(request.form['reg_password'])
			}
			mysql.query_db(query, data)
			return redirect('/success')

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/wall')
def the_wall():
		if not 'user_id' in session:
			return redirect('/')
		query = "SELECT first_name, last_name FROM users WHERE id = :user_id"
		data = {
			'user_id': session['user_id']
		}
		user = mysql.query_db(query, data)
		query = "SELECT messages.id as message_id, users.id as user_id, message, messages.created_at as time_string, DATE_FORMAT(messages.created_at, '%M %D, %Y - %h:%i %p') as created_at, CONCAT(first_name, ' ', last_name) as username FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
		messages = mysql.query_db(query)
		query = "SELECT message_id, users.id, comments.id as comment_id, comment, DATE_FORMAT(comments.created_at, '%M %D, %Y - %h:%i %p') as created_at, CONCAT(first_name, ' ', last_name) as username, user_id, comments.created_at as time_string FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.created_at ASC;"
		comments = mysql.query_db(query, data)
		now = datetime.datetime.now()
		return render_template('the_wall.html', user=user[0], messages = messages, comments = comments, now = now)

@app.route('/comms', methods=['POST'])
def process_comms():
	if request.form['action'] == 'message':
		query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
		data = {
			'message': request.form['user_message'],
			'user_id': session['user_id']
		}
		mysql.query_db(query, data)
	elif request.form['action'] == 'comment':
		query = "INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES (:comment, NOW(), NOW(), :message_id, :user_id)"
		data = {
			'comment': request.form['user_comment'],
			'user_id': session['user_id'],
			'message_id': int(request.form['message_id'])
		} 
		mysql.query_db(query, data)
	elif request.form['action'] == 'delete':
		query = "DELETE FROM comments WHERE message_id = :message_id"
		data = {
			'message_id': int(request.form['message_id'])
		}
		mysql.query_db(query, data)
		query = "DELETE FROM messages WHERE id = :message_id"
		mysql.query_db(query, data)
	elif request.form['action'] == 'delete-comment':
		query = "DELETE FROM comments WHERE id = :comment_id"
		data = {
			'comment_id': int(request.form['comment_id'])
		}
		mysql.query_db(query, data)
	return redirect('/wall')

app.run(debug=True)