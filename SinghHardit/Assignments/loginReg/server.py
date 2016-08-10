from flask import Flask, render_template,redirect,session, flash,request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secretKey"
mysql = MySQLConnector(app,'app')

@app.route("/")
def index():
	session['logged'] =False
	return render_template('index.html')

@app.route("/register")
def reg():
	return render_template('registration.html')

@app.route("/login", methods=['POST'])
def login():
	email = request.form['email']
	pwd = request.form['password']	
	query = "select * from users where email = :email limit 1"	
	
	if mysql.query_db(query,{"email": email}):
		data = mysql.query_db(query,{"email": email})
	else:
		return redirect("/register")

	if bcrypt.check_password_hash(data[0]['password'],pwd):
		session['logged']=True
		return redirect('/success')
	else: 
		flash("Invalid Password")
		return redirect("/")

@app.route("/registration", methods=['POST'])
def registration():	
	email = request.form['email']
	query = "select * from users where email = :email limit 1"	
	
	if mysql.query_db(query,{"email": email}):
		flash("Email already exists")
		return redirect('/register')

	def validate():	
		count = 0	
		if len(request.form['email'])<1:
			flash("Email cannot be empty")
			count+=1
		if len(request.form['first_name'])<2:
			flash("First name should be atleast two charachters long")
			count+=1		
		if len(request.form['last_name']) < 2:
			flash("Last name should be atleast two charachters long")
			count+=1			
		if len(request.form['password'])<8:
			flash("Password must be at least 8 characters")
			count+=1				
		if request.form['confirm'] != request.form['password']:
			flash("Confirm password must match password")
			count+=1
		if count ==0:
			return False
		else: 
			return True					
	
	if validate():
		return redirect("/register")
	else:
		query = "insert into users (email, first_name, last_name, password, created_at, updated_at) values (:email, :first_name, :last_name, :password, now(), now())"
		data = {
		'email':request.form['email'],
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'password': bcrypt.generate_password_hash(request.form['password']),				
		}	
		mysql.query_db(query,data)	
		session['logged'] = True
		return redirect('/success')	

@app.route("/logout")
def logout():
	return redirect("/")

@app.route('/success')
def sucess():
	if session['logged']:
		return render_template("success.html")
	else:
		flash("Not so easy brvah..lease log in first")
		return redirect("/")		

app.run(debug=True)
