from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import re

PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/result')
# def result():
#     return render_template("result.html")


@app.route('/process', methods=['POST'])
def process():
    formInfo = {
        "email": request.form['email'],
        "first name": request.form['fname'],
        "last name": request.form['lname'],
        "password": request.form['pass'],
        "password confirmation": request.form['confirmpass']
    }
    for ele in formInfo.items():
        if len(ele[1]) < 1:
            flash(ele[0] + ' is Required. \n', 'red')
    if formInfo['password'] != formInfo['password confirmation']:
        flash('Confirmation password must match password is Required.','red')
    if not PASS_REGEX.match(formInfo['password']):
        flash('Password minimum 8 characters, at least 1 Alphabet and 1 Number', 'red')
    if '_flashes' not in session:
        flash('Registration was successful!!!','green')
    # session.clear()
    return redirect("/")

app.run(debug=True) # run our servers
