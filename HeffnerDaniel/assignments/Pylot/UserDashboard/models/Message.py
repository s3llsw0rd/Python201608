from system.core.model import Model

class Message(Model):
	def __init__(self):
		super(Message, self).__init__()

	def get_content_by_user_id(self, id):
		if not id > 0:
			return False
		m_query = 'SELECT messages.id, message, messages.created_at as m_created_at, CONCAT(first_name, " ", last_name) as poster FROM messages JOIN users ON user_id = users.id WHERE recipient_id = :id ORDER BY m_created_at DESC;'
		m_data = { 'id': id }
		messages = self.db.query_db(m_query, m_data)
		for message in messages:
			c_query = 'SELECT comment, comments.created_at as c_created_at, CONCAT(first_name, " ", last_name) as commenter FROM comments JOIN users ON user_id = users.id WHERE message_id = :id ORDER BY c_created_at ASC;'
			c_data = { 'id': message['id'] }
			message['comments'] = self.db.query_db(c_query, c_data)
			message['m_created_at'] = message['m_created_at'].strftime('%b %d, %Y %I:%M %p')
			for comment in message['comments']:
				comment['c_created_at'] = comment['c_created_at'].strftime('%b %d, %Y %I:%M %p')
		return messages

	def new_message(self, info):
		if not id > 0:
			return False
		# TODO: Validation
		query = 'INSERT INTO messages (message, user_id, recipient_id) VALUES (:message, :user_id, :recipient_id)'
		return self.db.query_db(query, info)

	def new_comment(self, info):
		if not id > 0:
			return False
		# TODO: Validation
		query = 'INSERT INTO comments (comment, user_id, message_id) VALUES (:comment, :user_id, :message_id)'
		return self.db.query_db(query, info)

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