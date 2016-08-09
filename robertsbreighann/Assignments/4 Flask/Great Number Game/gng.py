import random

from flask import session, Flask, redirect, render_template
from flask import request


app = Flask(__name__)
app.secret_key = 'something'

@app.route('/')
def root():
  if not 'random' in session:
    session['random'] = random.randrange(1, 100)

  if not 'box_class' in session:
    session['box_class'] = 'bc_none'

  box_class = session['box_class']
  session['box_class'] = 'bc_none'

  return render_template('index.htm', box_class=box_class, box_contents=session['box_contents'])


@app.route('/process_guess', methods=['POST'])
def process_guess():
  guess = int(request.form['guess'])
  random = session['random']  
  session['box_class'] = 'bc_red'

  if guess < random:
    session['box_contents'] = 'Too low!'
  elif guess > random:
    session['box_contents'] = 'Too high!'
  else:
    session['box_class'] = 'bc_green'
    session['box_contents'] = '{} was the number!'.format(guess)
    session.pop('random')

  return redirect('/')

app.run(debug=True)

