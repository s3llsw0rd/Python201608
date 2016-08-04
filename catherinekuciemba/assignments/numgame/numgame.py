from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'superrrr secret'

@app.route('/', methods = ['GET', 'POST'])
def index():
    data = {}
    try:
        session['num']
    except:
        session['num'] = random.randrange(0, 101)

    try:
        print request.form
        guess = int(request.form['guess'])
        if guess == session['num']:
            data ={'event':'Correct'}
            data['box'] = 'green'
            data['correct'] = 'true'
            data['guess']=str(guess)
        elif guess < session['num']:
            data = {'event':'Nope! Too low'}
            data['box'] = 'red'
            data['guess']=str(guess)
        else:
            data = {'event':'Nope! Too high'}
            data['box'] = 'red'
            data['guess']=str(guess)
        print data
    except:
        data = {'event':'make a guess'}
        data['guess']='Please enter a number'
        print data

    return render_template('index.html', data = data)

@app.route('/reset', methods = ['GET'])
def reset():
    session['num'] = random.randrange(0, 101)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
