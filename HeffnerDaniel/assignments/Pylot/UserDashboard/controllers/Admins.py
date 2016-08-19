from system.core.controller import *

class Admins(Controller):
	def __init__(self, action):
		super(Admins, self).__init__(action)
		self.load_model('User')

	def admin(self):
		if 'user' not in session:
			return redirect('/')
		if session['user']['user_level'] != 9:
			return redirect('/logoff')
		users = self.models['User'].all_users()
		return self.load_view('/admin/admin.html', users=users)

	def new(self):
		if 'user' not in session:
			return redirect('/')
		if session['user']['user_level'] != 9:
			return redirect('/logoff')
		return self.load_view('/admin/new.html')

	def edit(self, id):
		if 'user' not in session:
			return redirect('/')
		if session['user']['user_level'] != 9:
			return redirect('/logoff')
		if id < 1:
			return redirect('/logoff')
		user = self.models['User'].one_user(id)
		if user:
			return self.load_view('/admin/edit.html', user=user)
		return redirect('/dashboard/admin')

	def destroy(self, id):
		if 'user' not in session:
			return redirect('/')
		if session['user']['user_level'] != 9:
			return redirect('/')
		self.models['User'].destroy_user(id)
		return redirect('dashboard/admin')

	def update(self, id):
		if 'user' not in session:
			return redirect('/')
		if session['user']['user_level'] != 9:
			return redirect('/')
		if not id:
			return redirect('/')
		if request.form['action'] == 'Update Information':
			self.models['User'].update_info(request.form)
		elif request.form['action'] == 'Update Password':
			if self.models['User'].update_pw(request.form) == 'error':
				flash('Passwords don\'t match')
		else:
			return redirect('/logoff')
		route = 'users/edit/' + str(id)
		return redirect(route)