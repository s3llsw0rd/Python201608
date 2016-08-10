from flask import Flask, render_template, request, redirect, flash, session
import re

app = Flask(__name__)
app.secret_key ='secret'

name_regex = re.compile(r'[0-9]')
pass_regex = re.compile(r'[A-Z0-9]')


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    session['val'] = {
        'email':request.form['email'],
        'first name': request.form['first_name'],
        'last name': request.form['last_name'],
        'password': request.form['password'],
        'confirm password': request.form['confirmpassword'],
        }
    for i in session['val']:
        if len(session['val'][i]) <1:
			flash('{0} Field may not be empty'.format(i))


    if name_regex.match(session['val']['first name']):
        flash('Your first name can not include a number')
    elif name_regex.match(session['val']['last name']):
        flash ('Your last name can not include a number')
    elif len(session['val']['password']) < 9:
        flash ('Your password must include at least 9 characters')
    elif session['val']['password'] != session['val']['confirm password']:
        flash('Your passwords do not match')
    else:
        render_template('results.html')
    #
    # session.pop('email_len')
    # session.pop('fname_len')
    # session.pop('lname_len')
    # session.pop('pwd_len')
    # session.pop('confpass_len')


    return redirect('/')

app.run(debug=True)
