from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'fortressOfSecurity'

@app.route('/')
def survey_home():
	return render_template('dojo_survey_home.html')

@app.route('/survey', methods = ['post'])
def create_survey():
	print 'Get Info Success'
	session['name'] = request.form['name']
	session['loc'] = request.form['loc']
	session['lang'] = request.form['lang']
	session['com'] = request.form['com']
	return redirect('/result')

@app.route('/result')
def show_result():
	return render_template('dojo_survey_result.html')
	




app.run(debug=True)


# I realize I didn't complete this the way it was intended. I frankly gave up on trying to get this to work without going through the Session section of the platform. Maybe I missed it, but I did not walk away from the material with anything like the understanding neccessary to complete this as intended. I downloaded the answersheet and could not figure out how I was supposed to come up with something that looked like that solution given what was presented in the material. Rather than copy and paste I skipped it, moved on, and came back. Super frustrating. Very timeconsuming.