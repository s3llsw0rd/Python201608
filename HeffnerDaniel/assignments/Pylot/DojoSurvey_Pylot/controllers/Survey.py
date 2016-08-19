from system.core.controller import *

class Survey(Controller):
	def __init__(self, action):
		super(Survey, self).__init__(action)
	def index(self):
		return self.load_view('index.html')

	def process(self):
		if not 'submits' in session:
			session['submits'] = 1
		else:
			session['submits'] += 1
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
		return redirect('/result')

	def result(self):
		return self.load_view('result.html', submits=session['submits'], name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

