from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.db = self._app.db

	def index(self):
		if 'user' in session:
			session.pop('user', None)
		return self.load_view('index.html')

	def success(self):
		if not 'user' in session:
			return redirect('/')
		return self.load_view('success.html', user=session['user'])

	def create_user(self):
		user_info = {
			'fname': request.form['fname'],
			'lname': request.form['lname'],
			'email': request.form['email'],
			'password': request.form['password'],
			'pwconfirm': request.form['pwconfirm'],
		}
		status = self.models['User'].new_user(user_info)
		if not status['success']:
			for lst in status['info']:
				flash(lst[0],lst[1])
			return redirect('/')
		else: 
			session['user'] = status['info']
			return redirect('/success')

	def login(self):
		user_info = {
			'email': request.form['email'],
			'password': request.form['password']
		}
		status = self.models['User'].login(user_info)
		if not status['success']:
			flash('Login failed. Please try again.', 'login')
			return redirect('/')
		else:
			session['user'] = status['info']
			return redirect('/success')





"""
A loaded model is accessible through the models attribute 
self.models['WelcomeModel'].get_users()

self.models['WelcomeModel'].add_message()
# messages = self.models['WelcomeModel'].grab_messages()
# user = self.models['WelcomeModel'].get_user()
# to pass information on to a view it's the same as it was with Flask

# return self.load_view('index.html', messages=messages, user=user)
"""
