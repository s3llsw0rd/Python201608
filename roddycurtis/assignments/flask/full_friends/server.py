from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'hahahahahahahahahahahahaha'

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def add():
	
	query = "INSERT INTO friends (first_name, last_name, occupation, email) VALUES ('{}', '{}', '{}','{}')".format(request.form['first_name'], request.form['last_name'], request.form['occupation'], request.form['email'])
	data = {
		'first_name':request.form['first_name'],
		'last_name':request.form['last_name'],
		'occupation':request.form['occupation'],
		'email':request.form['email']
    }

	mysql.query_db(query, data)
	
	return redirect('/')

@app.route(('/friends/<friend_id>'))
def update(friend_id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {
    	'id':friend_id
	}  
    
    friends = mysql.query_db(query,data) 
   
# ensure got bacck 1friend
# if not len(friends) =1:
# redirect('/')
flash(nice try sucka)
    
    return render_template('edit.html', friend=friends[0])
	    
@app.route(('/friends/<friend_id>/edit'),methods=['post'])
def edit(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, email= :email WHERE id = :id"
    data={
    		'first_name':request.form['first_name'],
    		'last_name':request.form['last_name'],
    		'occupation':request.form['occupation'],
    		'email':request.form['email'],
    		'id':friend_id
    	}  
   
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
