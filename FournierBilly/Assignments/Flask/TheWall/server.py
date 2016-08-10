from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key='ThisIsSecret'
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app,'walldb')
PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")

@app.route('/')
def index():
    if 'login' not in session:
        return render_template('login.html')
    return redirect('/wall')

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
        formData['password'] = bcrypt.generate_password_hash(formData['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password ,NOW(), NOW())"
        mysql.query_db(query, formData)

        query = "SELECT * FROM users WHERE email = :email"
        login_user = mysql.query_db(query, formData)
        session['login'] = login_user
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
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
    query = "SELECT * FROM users WHERE email = :email"
    login_user = mysql.query_db(query, data)
    if len(login_user) < 1:
        flash('Invalid email / password combo')
    if bcrypt.check_password_hash(login_user[0]['password'], data['password']):
        session['login'] = login_user
    return redirect('/wall')

@app.route('/wall')
def wall():
    if 'login' in session:
        query = 'SELECT * FROM users INNER JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC'
        session['msg'] = mysql.query_db(query)
        query = 'SELECT * FROM comments INNER JOIN users ON comments.user_id = users.id'
        session['comments'] = mysql.query_db(query)
        # for comment in session['comments']:
        #     if comment['message_id'] == msg['id']
        return render_template('index.html')
    else:
        flash('User failed to authenticate', 'red')
        return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    print 'this is the msg button'
    if 'msg' not in session:
        session['msg'] = []

    data = {
        "message": request.form['message'],
        'user_id': str(session['login'][0]['id'])
    }
    print data
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES ( :message, :user_id ,NOW(), NOW() )"
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    print 'this is the msg button'
    if 'comment' not in session:
        session['comment'] = []

    data = {
        'comment': request.form['comment'],
        'message_id': request.form['message_id'],
        'commenter_id':  session['login'][0]['id']
    }
    query = "INSERT INTO comments (comment, message_id , user_id, created_at, updated_at) VALUES ( :comment, :message_id , :commenter_id, NOW(), NOW() )"
    mysql.query_db(query, data)
    return redirect('/wall')


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
