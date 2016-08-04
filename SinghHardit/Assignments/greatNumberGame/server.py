from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def rand():
    if not 'number' in session:
        session['number'] = random.randrange(1,100)
        session['wrong'] = "hide"        
        session['right'] = "hide"               
    return render_template('index.html')   

@app.route('/answer', methods=['POST'])
def result():
    guess = int(request.form['guess'])
    print guess
    if guess > session['number']:
        session['wrong'] = "high"        
        session['right'] = "hide"               
        return redirect('/')
    elif guess < session['number']:        
        session['wrong'] = "low"        
        session['right'] = "hide"                
        return redirect('/')
    elif guess == session['number']:
        session['wrong'] = "hide"        
        session['right'] = "right"        
        session['form'] = "hide "                  
        return redirect('/')

@app.route('/right',methods=['POST'])
def right():    
    session.pop('number')
    session['form'] = "show"
    return redirect ('/')

app.run(debug=True)        

        