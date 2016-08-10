from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM friends")
	return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():   
	query = "insert into friends (first_name,last_name,occupation,created_at,updated_at) values (:first_name,:last_name,:occupation,now(),now())"
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation']
	}
	mysql.query_db(query,data)
	
	return redirect('/')

@app.route("/friends/<id>")
def editDisplay(id):
	data = {"id": id}
	friend = mysql.query_db("SELECT * FROM friends where id = :id",data)
	print friend[0]['first_name']
	return render_template("edit.html", friend=friend)

@app.route("/friends/<id>/edit", methods=['POST'])
def edit(id):	
	query = "update friends set first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = now() where id = :id"
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation'], 
		"id": id
	}
	mysql.query_db(query,data)
	return redirect("/")

@app.route("/delete/<id>")
def delete(id):
	query = 'delete from friends where id = :id'
	data = {"id": id}
	mysql.query_db(query,data)
	return redirect("/")

app.run(debug=True)