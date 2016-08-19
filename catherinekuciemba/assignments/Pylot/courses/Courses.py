from system.core.controller import *
class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html',courses=courses)

    def add(self):
            course_details = {
                'course_name': request.form['course_name'],
                'description': request.form['description']
            }
            # if len('course_name')<= 2
            #     return redirect('/')
            # if len['description']<= 2
            #     return redirect('/')
            # else
            course_id =  self.models['Course'].add_course(course_details)

            return redirect('/')

    def destroy(self, id):
    # Note how we access the model using self.models
        info = self.models['Course'].get_course_by_id(id)
        return self.load_view('destroy.html', info=info)

    def remove(self, id):
        self.models['Course'].delete_course(id)

        return redirect('/')
