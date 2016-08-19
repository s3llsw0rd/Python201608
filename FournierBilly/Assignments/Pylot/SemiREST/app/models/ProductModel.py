"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class ProductModel(Model):
    def __init__(self):
        super(ProductModel, self).__init__()

    def get_products(self):
        query = "SELECT * from products"
        return self.db.query_db(query)

    def get_product(self,id):
        data = { 'id' : id }
        query = "SELECT * from products WHERE products.id = :id LIMIT 1"
        product = self.db.query_db(query,data)
        return product[0]

    def create_product(self, product_info):
        errors =[]
        try:
            price = float(product_info['price'])
        except ValueError:
            errors.append('Price must be a dollar value')
        if len(product_info['name']) < 1:
            errors.append('Must have name')
        if len(product_info['price']) < 1:
            errors.append('Must have a price')
        if len(errors) > 0:
            return errors
        print product_info
        data = {
            'name' : product_info['name'],
            'description' : product_info['desc'],
            'price' : price
        }
        print 'test2'
        query = 'INSERT INTO products (name, description, price, created_at, updated_at) VALUE (:name, :description, :price, NOW(), NOW())'

        self.db.query_db(query,data)

        return False

    def delete_product(self, id):
        data = {'id': id}
        query = 'DELETE FROM products WHERE products.id = :id '
        self.db.query_db(query,data)
        return True

    def update_product(self,id,updated_info):
        data = {
            'id' : id,
            'name' : updated_info['name'],
            'description' : updated_info['desc'],
            'price' : updated_info['price']
         }
        query = 'UPDATE products SET name=:name, description=:description, price=:price, updated_at=NOW() WHERE id=:id LIMIT 1;'
        self.db.query_db(query,data)
        return True

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
