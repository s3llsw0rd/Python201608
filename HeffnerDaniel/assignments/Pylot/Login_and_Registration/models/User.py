from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
NAME_REGEX = re.compile(r'^[a-zA-z\-\.]*$')

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def new_user(self, user_info):
		errors = []
		if len(user_info['fname'])<2:
			errors.append(['First name must be 2 characters or longer.', 'fname'])
		if not NAME_REGEX.match(user_info['fname']):
			errors.append(['Names may only include letters, hyphens, and periods.', 'fname'])
		if len(user_info['lname'])<2:
			errors.append(['Last name must be 2 characters or longer.', 'lname'])
		if not NAME_REGEX.match(user_info['lname']):
			errors.append(['Names may only include letters, hyphens, and periods.', 'lname'])
		if user_info['email'] == '':
			errors.append(['You\'ll need an email to login.', 'email'])
		elif not EMAIL_REGEX.match(user_info['email']):
			errors.append(['Please enter a valid email address.', 'email'])
		else:
			query = 'SELECT * FROM users WHERE email = :email'
			data = {'email': user_info['email'].lower()}
			if len(self.db.query_db(query, data)) > 0:
				errors.append(['This email is already in use.', 'email'])
		if user_info['password'] == '':
			errors.append(['You\'ll need a password in order to login.', 'password'])
		elif not len(user_info['password']) > 7:
			errors.append(['Passwords must be at least 8 characters.', 'password'])
		if user_info['password'] != user_info['pwconfirm']:
			errors.append(['Passwords didn\'t match; confirmation failed.', 'password'])

		if len(errors) > 0:
			return {'success': False, 'info': errors}
		else:
			query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (:fname, :lname, :email, :password)'
			pw = user_info['password']
			hashed_pw = self.bcrypt.generate_password_hash(pw)
			data = {
				'fname': user_info['fname'],
				'lname': user_info['lname'],
				'email': user_info['email'].lower(),
				'password': hashed_pw
			}
			new_id = self.db.query_db(query, data)
			get_new_user = 'SELECT * FROM users WHERE id = :id'
			new_data = { 'id': new_id }
			user = self.db.query_db(get_new_user, new_data)
			return { 'success': True, 'info': user[0] }


	def login(self, user_info):
		password = user_info['password']
		login_query = 'SELECT * FROM users WHERE email = :email'
		login_data = {'email': user_info['email'].lower()}
		user = self.db.get_one(login_query, login_data)
		if user:
			if self.bcrypt.check_password_hash(user['password'], password):
				user = self.db.query_db(login_query, login_data)
				return {'success': True, 'info': user[0]}
		return {'success': False, 'info': ''}



	"""
	Below is an example of a model method that queries the database for all users in a fictitious application
	
	Every model has access to the "self.db.query_db" method which allows you to interact with the database

	def get_users(self):
		query = "SELECT * from users"
		return self.db.query_db(query)

	def get_user(self):
		query = "SELECT * from users where id = :id"
		data = {'id': 1}
		return self.db.get_one(query, data)

	def add_message(self):
		sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
		data = {'message': 'awesome bro', 'users_id': 1}
		self.db.query_db(sql, data)
		return True
	
	def grab_messages(self):
		query = "SELECT * from messages where users_id = :user_id"
		data = {'user_id':1}
		return self.db.query_db(query, data)

	"""