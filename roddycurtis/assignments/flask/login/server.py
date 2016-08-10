from flask import Flask, request, redirect, render_template, flash,session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'logindb')
app.secret_key = 'hahaha'

@app.route('/')
def index():
    session['logged']=False
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/login", methods=['POST'])
def login():
  
   email = request.form['email']
   password = request.form['password']	
   query = "SELECT * FROM registration where email=:email"

   
   if mysql.query_db(query,{"email": email}):
 		data = mysql.query_db(query,{"email": email})
   else:
 		return redirect("/register")

   if bcrypt.check_password_hash(data[0]['password'],password):
 		session['logged']=True
 		return redirect('/loggedin')
   else: 
 		flash("Please Enter A Different Password")
 		return redirect("/")
    
   return render_template('index.html')

@app.route('/loggedin')
def loggedin():
    if session['logged']:
        return render_template('loggedin.html')
    else:
       return redirect('/')

@app.route('/create', methods=['POST'])
def check():
   valid=0
   if len(request.form['first_name'])<2:
       flash('I doubt that is your real first name')
       valid+=1
   if len(request.form['last_name'])<2:
       flash('No Way!!!!')
       valid+=1
   if len(request.form['email'])<1:
       flash('Please Enter A Valid Email Address')
       valid+=1
   if len(request.form['password'])<8:
       flash('Your Password Needs To Be 8 Characters')
       valid+=1


   if valid>0:
       return redirect('/')

   else:
    query = "INSERT INTO registration (first_name,last_name,email,password) VALUES (:first_name, :last_name, :email, :password)"
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
       
    }
    session['logged']=True
    mysql.query_db(query, data)    
    return redirect('/loggedin')

app.run(debug=True)
