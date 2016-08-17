from system.core.model import Model

class Product(Model):
	def __init__(self):
		super(Product, self).__init__()

	def get_all_products(self):
		query = 'SELECT * FROM products ORDER BY id DESC'
		return self.db.query_db(query)

	def get_one_product(self, id):
		query = 'SELECT * FROM products WHERE id = :id'
		data = { 'id': id }
		return self.db.query_db(query, data)

	def update_product(self, info):
		query = 'UPDATE products SET name=:name, description=:description, price=:price WHERE id=:id'
		return self.db.query_db(query, info)

	def create_product(self, info):
		query = 'INSERT INTO products (name, description, price) VALUES (:name, :description, :price)'
		return self.db.query_db(query, info)

	def destroy_product(self, id):
		query = 'DELETE FROM products WHERE id = :id'
		data = { 'id': id}
		return self.db.query_db(query, data)





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