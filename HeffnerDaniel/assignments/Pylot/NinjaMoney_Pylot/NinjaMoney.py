from system.core.controller import *
import random

class NinjaMoney(Controller):
	def __init__(self, action):
		super(NinjaMoney, self).__init__(action)
	def index(self):
		if not 'gold' in session:
			session['gold'] = 0
		if not 'activities' in session:
			session['activities'] = []
		return self.load_view('index.html', gold=session['gold'], activities=session['activities'])

	def process(self):
		if request.form['building'] == 'farm':
			session['earn'] = random.randrange(10,21)
			session['activities'].append({'color':'green', 'text':'Earned '+ str(session['earn']) + ' gold from the farm!'})
		elif request.form['building'] == 'cave':
			session['earn'] = random.randrange(5,11)
			session['activities'].append({'color':'green', 'text':'Earned '+ str(session['earn']) + ' gold from the cave!'})
		elif request.form['building'] == 'house':
			session['earn'] = random.randrange(2,6)
			session['activities'].append({'color':'green', 'text':'Earned '+ str(session['earn']) + ' gold from the house!'})
		elif request.form['building'] == 'casino':
			session['earn'] = random.randrange(-50,51)
			if session['earn'] < 0:
				session['activities'].append({'color':'red', 'text':'Lost '+ str(session['earn']) + ' gold at the casino...'})
			elif session['earn'] > 0:
				session['activities'].append({'color':'green', 'text':'Won '+ str(session['earn']) + ' gold at the casino!'})
			else:
				session['activities'].append({'color':'', 'text':'Broke even at the casino.'})
		session['gold'] += session['earn']
		return redirect('/')

