from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = 'secret'

def validate():
    if request.form['first_name'] == '':
        flash('Name cannot be blank', 'first_NameError')
        pass
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('Name cannot have numbers', 'first_NameError')
        pass
    else:
        pass

    if request.form['last_name'] == '':
        flash('Name cannot be blank', 'last_NameError')
        pass
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Name cannot have numbers', 'last_NameError')
        pass
    else:
        pass

    if request.form['occupation'] == '':
        flash('Occupation cannot be blank', 'occupation_Error')
        pass
    else:
        pass

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', list=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data={
        "id": id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "occupation": request.form['occupation'],
    }

    if validate() == False:
        return redirect('/')
    else:
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def edit(id):
    print id
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = NOW() WHERE id = :id"
    data={
        "id": id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "occupation": request.form['occupation'],
    }
    if validate() == False:
        return redirect('/')
    else:
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def viewEdit(id):

    query = "SELECT * FROM friends WHERE id = :id"
    data={
        "id": id
    }
    friendData = mysql.query_db(query, data)

    print friendData
    return render_template('edit.html', friend=friendData[0])

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data={
        "id": id
    }
    print query
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
