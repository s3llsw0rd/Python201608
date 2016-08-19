from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        course_data = self.models['Course'].get_courses()
        return self.load_view('index.html', course_data = course_data)

    def add(self):
        if len(request.form['name']) <15:
            flash('Course name has to be at least 15 characters')
            return redirect('/')
        course_data = {
            'name': request.form['name'],
            'description': request.form['description'] 
        }
        self.models['Course'].add_course(course_data)
        return redirect("/")
   
    def remove_page(self,id):
        course_info = self.models['Course'].get_course(id)
        return self.load_view('remove.html',course_info=course_info[0])
    
    def delete(self,id):
        self.models['Course'].delete_course(id)
        return redirect('/')  
              


        