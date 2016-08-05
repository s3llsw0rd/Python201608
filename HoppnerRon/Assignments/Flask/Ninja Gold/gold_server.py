from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'duanesworld'

@app.route('/', methods = ['get', 'post'])
def index():
	session['gold'] = 0
	session['tansaction'] = 0
	return render_template('ninja_gold.html')







app.run(debug=True)