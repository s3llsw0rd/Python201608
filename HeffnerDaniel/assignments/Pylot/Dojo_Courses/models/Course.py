from system.core.model import Model

class Course(Model):
	def __init__(self):
		super(Course, self).__init__()
	
	def get_all_courses(self):
		return self.db.query_db('SELECT * FROM course ORDER BY id DESC')

	def add_course(self, course):
		query = 'INSERT INTO course (name, description) VALUES (:name, :description);'
		data = {
			'name': course['name'],
			'description': course['description']
		}
		return self.db.query_db(query, data)

	def destroy_course(self, id):
		query = 'DELETE FROM course WHERE id = :id'
		data = { 'id': id }
		return self.db.query_db(query, data)

	def get_course_by_id(self, id):
		query = 'SELECT * FROM course WHERE id = :id'
		data = {'id': id}
		return self.db.query_db(query, data)