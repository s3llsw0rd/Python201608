from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')   # display all of the friends on the index.html page
def index():
	query = "SELECT * FROM friends"                           # define your query
	friends = mysql.query_db(query)                           # run query with query_db()
	return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])	# handle the add friend form submit and create friend in the DB
def create():
	# Query String
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	# KEEP data AWAY from query string
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation']
	}
	# Run the query
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<friend_id>/edit', methods=['POST'])	# Display the edit friend page for the particular friend
def edit(friend_id):
	query = "SELECT * FROM friends WHERE id = :specific_id"
	data = {'specific_id': friend_id}
	friend = mysql.query_db(query, data)
	return render_template('edit_friend.html', friend = friend[0])

@app.route('/friends/<friend_id>', methods=['POST'])	# Handle the edit friend form submit and update the friend in the DB
def update(friend_id):
	query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, occupation=:occupation, updated_at=NOW() WHERE id=:specific_id;"
	data = {
		'specific_id': friend_id,
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation']
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<friend_id>/delete', methods=['POST'])	# Delete the friend from the DB
def destroy(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = { 'id': friend_id }
	mysql.query_db(query, data)
	return redirect('/')

# look up what restful routes are

app.run(debug=True)