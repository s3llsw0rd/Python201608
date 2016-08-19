from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('Message')
		self.load_model('User')

	def signin(self):
		return self.load_view('/users/signin.html')

	def register(self):
		return self.load_view('/users/register.html')

	def dashboard(self):
		if not 'user' in session:
			return redirect('/')
		users = self.models['User'].all_users()
		if session['user']['user_level'] == 9:
			return self.load_view('/admin/admin.html', users=users)
		return self.load_view('/users/dashboard.html', users=users)

	def edit(self):
		if not 'user' in session:
			return redirect('/')
		user = self.models['User'].one_user(session['user']['id'])
		return self.load_view('/users/edit.html', user=user)

	def show(self, id):
		if not 'user' in session:
			return redirect('/')
		user = self.models['User'].one_user(id)
		content = self.models['Message'].get_content_by_user_id(id)
		return self.load_view('/users/show.html', user=user, content=content)

	def logoff(self):
		if 'user' in session:
			session.pop('user', None)
		return redirect('/')

	def login(self):
		user = self.models['User'].user_login(request.form)
		if user:
			session['user'] = user
			if user['user_level'] == 9:
				return redirect('/dashboard/admin')
			else: 
				return redirect('/dashboard')
		return redirect('/signin')

	def create(self):
		user = self.models['User'].insert_user(request.form)
		if not user:
			return redirect('/')
		if 'user' in session:
			if session['user']['user_level'] == 9:
				return redirect('/dashboard/admin')
		else:
			session['user'] = user
			if user['user_level'] == 9:
				return redirect('/dashboard/admin')
			else:
				return redirect('/dashboard')

	def update(self):
		if 'user' not in session:
			return redirect('/')
		if request.form['action'] == 'Update Information':
			self.models['User'].update_info(request.form)
		elif request.form['action'] == 'Update Password':
			if self.models['User'].update_pw(request.form) == 'error':
				flash('Passwords don\'t match')
		elif request.form['action'] == 'Update Description':
			self.models['User'].update_desc(request.form)
		else:
			return redirect('/logoff')
		return redirect('/users/edit')