""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    
    def add_course(self, course_data):
        sql = "INSERT into courses (name, description, created_at, updated_at) values(:name, :description, NOW(), NOW())"
        self.db.query_db(sql, course_data)
        return True
    
    def get_courses(self):
        query = "SELECT * from courses order by created_at desc"
        return self.db.query_db(query)
    
    def get_course(self,id):
        query = 'SELECT * from courses where id = :id'
        data = {'id':id}
        return self.db.query_db(query,data)
    
    def delete_course(self,id):
        query = "DELETE from courses where id =:id"
        data = {'id':id}
        self.db.query_db(query,data)
        return True

            



