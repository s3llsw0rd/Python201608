from system.core.controller import *
import random
import string

class RandomWord(Controller):
	def __init__(self, action):
		super(RandomWord, self).__init__(action)
		self.letters = list(string.ascii_letters)
	def index(self):
		if not 'word' in session:
			session['attempt'] = 0
			self.process()
		return self.load_view('index.html', attempt=session['attempt'], word=session['word'])

	def process(self):
		session['word'] = ''
		for c in range(14):
			if random.random() < 0.5:
				session['word'] += self.letters[random.randrange(0,51)]
			else:
				session['word'] += str(random.randrange(0,9))
		session['attempt'] += 1
		return redirect('/')

