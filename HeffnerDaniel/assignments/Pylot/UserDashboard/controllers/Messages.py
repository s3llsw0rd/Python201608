from system.core.controller import *

class Messages(Controller):
	def __init__(self, action):
		super(Messages, self).__init__(action)
		self.load_model('Message')

	def create(self, id):
		if not 'user' in session:
			return redirect('/')
		if not id > 0:
			return False
		info = {
			'message': request.form['message'],
			'user_id': session['user']['id'],
			'recipient_id': id
		}
		self.models['Message'].new_message(info)
		route = '/users/show/' + id
		return redirect(route)

	def comment(self, id):
		if not 'user' in session:
			return redirect('/')
		if not id > 0:
			return False
		print request.form
		info = {
			'comment': request.form['comment'],
			'user_id': session['user']['id'],
			'message_id': request.form['msg_id']
		}
		self.models['Message'].new_comment(info)
		route = '/users/show/' + id
		return redirect(route)