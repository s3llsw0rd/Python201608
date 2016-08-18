"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('UserModel')
        #self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def register(self):
        register_data = request.form
        user = self.models['UserModel'].register_user(register_data)
        if user['status'] == True:
            return self.load_view('success.html', user=user)
        else:
            for msg in user['errors']:
                flash(msg, 'regis_errors')
            return redirect('/')
        return redirect('/')

    def login(self):
        register_data = request.form
        user = self.models['UserModel'].login_user(register_data)
        print user
        if user['status'] == False:
            for msg in user['errors']:
                flash(msg, 'regis_errors')
            return redirect('/')
        else:
            return self.load_view('success.html', user=user['user'])
