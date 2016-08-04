from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="SuperSecretNinjaPhrase"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	errors = 0
	if len(request.form['name']) < 1:
		flash('Name cannot be empty!')
		errors += 1
	if len(request.form['comment']) < 1:
		flash('Comment cannot be empty!')
		errors += 1
	if len(request.form['comment']) > 120:
		flash('Comment cannot be longer than 120 characters!')
		errors += 1
	if errors > 0:
		return redirect('/')
	else:
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
		return redirect('/result')

@app.route('/result')
def result():
	return render_template('result.html')

app.run(debug=True)