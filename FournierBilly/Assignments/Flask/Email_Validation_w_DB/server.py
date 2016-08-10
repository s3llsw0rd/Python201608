from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'mydb')


@app.route('/')
def index():
    email_list = mysql.query_db("SELECT * FROM email_validations")
    return render_template('index.html',all_emails=email_list)

# @app.route('/')
# def index():
#     # friends = mysql.query_db("SELECT * FROM friends")
#     # print friends
#
#     query = "SELECT * FROM friends"                           # define your query
#     friends = mysql.query_db(query)
#     return render_template('index.html', all_friends=friends)

import re
@app.route('/process', methods=['POST'])
def create():
    email = request.form['email']
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
    	flash('Enter a valid email', 'red')
    else:
        msg = "The email address you entered (" + email + ") is a VALID email address! Thank you!"
        flash(msg, 'green')
        query = "INSERT INTO email_validations (email) VALUES (:email)"
        data = {
                 'email': request.form['email']
               }
        mysql.query_db(query, data)

    # query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # data = {
    #          'first_name': request.form['first_name'],
    #          'last_name':  request.form['last_name'],
    #          'occupation': request.form['occupation']
    #        }
    # mysql.query_db(query, data)
    return redirect('/')

# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
#
# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query)
#     return redirect('/')

app.run(debug=True)
