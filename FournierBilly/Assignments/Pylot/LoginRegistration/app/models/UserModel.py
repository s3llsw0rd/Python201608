"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()

    def register_user(self,user_data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if len(user_data['fname']) < 1:
            errors.append('Must include a first name')
        if len(user_data['lname']) < 1:
            errors.append('Must include a last name')
        if len(user_data['email']) < 1:
            errors.append('Must include an email address')
        elif not EMAIL_REGEX.match( user_data['email'] ):
            errors.append('Must include a valid email address')
        if len(user_data['pwd']) < 4:
            errors.append('Password to short')
        elif user_data['pwd'] != user_data['pwdc']:
            errors.append('Password must match confirmation password')
        if len(errors) > 0:
            return {"status": False, "errors": errors}


        password = user_data['pwd']
        hashed_pw = self.bcrypt.generate_password_hash(password)
        data = {
            'first_name' : user_data['fname'],
            'last_name' : user_data['lname'],
            'email' :   user_data['email'],
            'password' : hashed_pw
        }
        query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUE(:first_name, :last_name, :email, :password, NOW(), NOW())'
        self.db.query_db(query, data)
        user = self.db.query_db('SELECT * FROM users ORDER BY users.id DESC LIMIT 1')
        # return { "status": True, "user": None }
        return { "status": True, "user": user[0] }

    def login_user(self, user_data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if len(user_data['email']) < 1:
            errors.append('Must include an email address')
        elif not EMAIL_REGEX.match( user_data['email'] ):
            errors.append('Must include a valid email address')
        if len(user_data['pwd']) < 4:
            errors.append('Password to short')
        if len(errors) > 0:
            return {"status": False, "errors": errors}

        data = { 'email' : user_data['email'] }
        query = 'SELECT * FROM users WHERE users.email = :email LIMIT 1'
        user = self.db.query_db(query, data)

        if len(user)==1:
            user=user[0]
            if self.bcrypt.check_password_hash(user['password'], user_data['pwd']):
                return {"status": True, "user": user}
        errors.append('email/password combination invalid')
        return {"status": False, "errors": errors}



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
