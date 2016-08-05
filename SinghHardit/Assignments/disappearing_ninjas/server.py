from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def main(name=None):
	dictionary = { 	'orange': "img/michelangelo.jpg",
		'red': "img/raphael.jpg",
		'purple': "img/donatello.jpg",
		'blue': "img/leonardo.jpg",		
	}
	
	if name in dictionary:
		file = 	 [dictionary[name]]
	elif name == "ninja":
		file = dictionary.values()
	else: 
		file = None		
	
	return render_template('index.html',file =file)

app.run(debug=True)
