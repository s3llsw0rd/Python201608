
from system.core.model import Model
class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM course")

    def get_course_by_id(self, id):
        # pass data to the query like so
        query = "SELECT * FROM course WHERE id = :id"
        data = { 'id': id}
        potential_course = self.db.query_db(query, data)
        if len(potential_course) != 1: return None
        return potential_course[0]

    def add_course(self, course):
        query = "INSERT INTO course (course_name, description, created_at) VALUES (:course_name, :description, NOW())"
        data = { 'course_name': course['course_name'], 'description': course['description'] }
        return self.db.query_db(query, data)


    def delete_course(self, id):
        query = "DELETE FROM course WHERE id = :id"
        data = { "id": id }
        self.db.query_db(query, data)

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
