"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
        if 'data' not in session:
            session['data'] = {}
        if 'count' not in session:
            session['count'] = 0


    def index(self):
        return self.load_view('index.html')

    def process(self):
        session['count'] += 1
        data = {
            'name' : request.form['name'],
            'location' : request.form['location'],
            'language' : request.form['language'],
            'comment' : request.form['comment'],
            'count' : session['count']
        }
        session['data'] = data
        return redirect('/result')
    def result(self):
        return self.load_view('result.html',
                                name=session['data']['name'],
                                location=session['data']['location'],
                                language=session['data']['language'],
                                comment=session['data']['comment'],
                                count=session['count'])
