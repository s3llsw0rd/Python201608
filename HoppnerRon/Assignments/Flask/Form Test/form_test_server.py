from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# index route will handle form render
@app.route('/')
def index():
	return render_template('index.html')

# POST route will handle form submission, waiting for a POST request to /users
@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/show') #redirects form back to the '/show' route where we can display session summary and not submit multiple requests.

@app.route('/show')
def show_user():
	return render_template('user.html')

app.run(debug=True)
