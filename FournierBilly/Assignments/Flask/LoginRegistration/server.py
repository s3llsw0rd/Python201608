from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key='ThisIsSecret'
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app,'loginregistration')
PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")

@app.route('/')
def index():
    # query = "SELECT * FROM friends"
    # friends = mysql.query_db(query)
    if 'login' not in session:
        session['login'] = False
    if session['login'] == True:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session['login'] = False
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    print 'test'
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    for ele in data.items():
        if len(ele[1]) < 1:
            flash(ele[0] + ' is Required. \n', 'red')
            return redirect('/')

    # pw = bcrypt.generate_password_hash(data['password'])
    # query = "SELECT users.email, users.password FROM users WHERE users.email = '" + data['email'] + "' LIMIT 1"
    query = "SELECT users.email, users.password FROM users WHERE email = :email"
    print query
    login_user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(login_user[0]['password'], data['password']):
        session['login'] = True
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    formData = {
        "email": request.form['email'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "password": request.form['password'],
        "password confirmation": request.form['password_confirmation']
    }

    for ele in formData.items():
        if len(ele[1]) < 1:
            flash(ele[0] + ' is Required. \n', 'red')
    if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', formData['email']):
        flash('Valid Email Required', 'red')
    if formData['password'] != formData['password confirmation']:
        flash('Confirmation password must match password is Required.','red')
    if not PASS_REGEX.match(formData['password']):
        flash('Password minimum 8 characters, at least 1 Alphabet and 1 Number', 'red')
    if '_flashes' not in session:
        session['login'] = True
        formData['password'] = bcrypt.generate_password_hash(formData['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password ,NOW(), NOW())"
        mysql.query_db(query, formData)
    return redirect('/')



# @app.route('/friends', methods=['POST'])
# def create():
#     query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation']
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
#
# @app.route('/friends/<id>/edit')
# def edit(id):
#     query = "SELECT * FROM friends WHERE friends.id = " + id
#     friend = mysql.query_db(query)
#     return render_template('edit.html', all_friends=friend)
#
# @app.route('/friends/<id>', methods=['POST'])
# def update(id):
#     print 'testing'
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'id': id,
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation']
#
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
#
# @app.route('/friends/<id>/delete', methods=['POST'])
# def delete(id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': id}
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)
