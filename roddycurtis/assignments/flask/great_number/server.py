from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
	number=session['number']
	if not 'number'in session:
			session['number']=random.randint(1,100)
			session['wrong']="hide"
			session['right']="hide"
	print number
	return render_template('index.html')

@app.route('/answer',methods=['POST'])
def answer():
	
    guess = int(request.form['guess'])
    print guess
    number=session[number]
    session['pybox']='red'

    if guess<random:
    	'Too Low'
    elif guess>random:
    	'Too High'
    else:
    	session['pybox']='green'
    	'Your Right'






    return redirect('/')
app.run(debug=True)