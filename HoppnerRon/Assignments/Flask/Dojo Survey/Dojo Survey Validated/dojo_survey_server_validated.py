from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'fortressOfSecurity'

@app.route('/')
def survey_home():
	return render_template('dojo_survey_home_validated.html')

@app.route('/survey', methods = ['post'])
def create_survey():
	session['name'] = request.form['name']
	session['loc'] = request.form['loc']
	session['lang'] = request.form['lang']
	session['com'] = request.form['com']

	if len(request.form['name']) < 1:
		flash('Name cannot be blank')
		return redirect('/')
	else:
		flash('I like that name.')


	if len(request.form['com']) < 1:
		flash('Comment cannot be blank.')
		return redirect('/')
	elif len(request.form['com']) > 121:
		flash('Whoa. Too much. Comments cannot be more than 120 characters')
	else:
		flash('Thanks for your thoughts.')

	return redirect('/result')

@app.route('/result')
def show_result():
	return render_template('dojo_survey_result_validated.html')
	




app.run(debug=True)
