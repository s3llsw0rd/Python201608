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
    return render_template('index.html')


app.run(debug=True)
