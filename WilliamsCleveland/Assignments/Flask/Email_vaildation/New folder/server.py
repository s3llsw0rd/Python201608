from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector


import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

mysql = MySQLConnector(app,'mydb')

@app.route('/', methods=['GET'])
def index():
    users = mysql.query_db("SELECT * FROM users")
    print users
    return render_template('index.html',  users=users)


@app.route('/create', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
        # validate email using python: request.form['email']
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
        return redirect('/')
    
    flash("Success!")
    query =  "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW());"
    data = {
             'email': request.form['email'], 
           }
    email_id = mysql.query_db(query, data)
    print email_id
        
    return redirect('/')


app.run(debug=True)