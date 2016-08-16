from system.core.controller import *
import random

class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)
		self.load_model('Course')

	def index(self):
		courses = self.models['Course'].get_all_courses()
		return self.load_view('index.html', courses=courses)

	def add(self):
		if request.form['name'] == '':
			flash('Courses must have a name!')
			return redirect('/')
		course = {
			'name': request.form['name'],
			'description': request.form['description']
		}
		self.models['Course'].add_course(course)
		return redirect('/')

	def destroy(self, id):
		course = self.models['Course'].get_course_by_id(id)
		print course
		return self.load_view('destroy.html', course=course[0])

	def delete(self, id):
		self.models['Course'].destroy_course(id)
		return redirect('/')

