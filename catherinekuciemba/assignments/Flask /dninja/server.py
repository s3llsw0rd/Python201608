from flask import Flask, render_template
app = Flask(__name__)

turtles = {
	'blue': 'leonardo',
	'orange': 'michelangelo',
	'red': 'raphael',
	'purple': 'donatello'
}



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def all():
	image = []
	for key in turtles:
		image.append(turtles[key])
	return render_template('ninjas.html', image=image)

@app.route('/ninja/<ncolor>')
def color(ncolor):
	image = []
	if ncolor in turtles:
		image.append(turtles[ncolor])
	else:
		image.append('notapril')
	return render_template('ninjas.html', image=image)

app.run(debug=True)
