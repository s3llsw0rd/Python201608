from flask import Flask, session, flash, render_template, request, redirect
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key='secret'
mysql = MySQLConnector(app, 'email_validation')

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def create():
    if request.form['email'] == '':
        flash('Email cannot be blank', 'red')
    elif  emailRegex.match(request.form['email']):
        flash('Invalid email address', 'red')
    else:
        email = request.form['email']
        session['email'] = email
        query = "INSERT INTO email_address (email, created_on, updated_on) VALUES ('{}', NOW(), NOW())".format(session['email'])
        print query
        email = mysql.query_db(query)
    return redirect('/success')

@app.route('/success')
def entries():
    query = "SELECT * FROM email_address"                           # define your query
    email_address = mysql.query_db(query)                           # run query with query_db()
    return render_template('success.html', all_email=email_address)


app.run(debug=True)
