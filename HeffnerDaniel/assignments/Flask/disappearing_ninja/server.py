from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'my_secret_key'

colors = {
	'blue': 'leonardo',
	'orange': 'michelangelo',
	'red': 'raphael',
	'purple': 'donatello'
}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def allfour():
	ninjapics = []
	for key in colors:
		ninjapics.append(colors[key])
	return render_template('ninjas.html', ninjapics=ninjapics)

@app.route('/ninja/<ninja_color>')
def ninja(ninja_color):
	ninjapics = []
	if ninja_color in colors:
		ninjapics.append(colors[ninja_color])
	else:
		ninjapics.append('notapril')
	return render_template('ninjas.html', ninjapics = ninjapics)

app.run(debug = True)