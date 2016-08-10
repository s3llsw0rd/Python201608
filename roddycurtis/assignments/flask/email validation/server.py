from flask import Flask, session, flash, render_template, request, redirect
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'email_val')
app.secret_key='password'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if not EMAIL_REGEX.match(request.form['email']):
        
        flash('{} is Not Valid!!!'.format(request.form['email']), "emailerrors")
        return redirect('/')
    else:
        email = request.form['email']
        session['email'] = email
       
        query =  "INSERT INTO valid(email) VALUES(:email)"
        data = { 'email' : session['email']}
        email_id = mysql.query_db(query, data)
    return redirect('/results')

@app.route('/results')
def results():
    query = "SELECT * FROM valid"
    emails=mysql.query_db(query)   
    print emails
    return render_template('results.html',all_emails=emails)



app.run(debug=True)



