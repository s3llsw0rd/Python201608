from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')   
def index():
  return render_template('landing_page_index_bar.html', name="Breigh Ann")


@app.route('/ninjas')
def ninjas():
  return render_template('landing_page_ninjas_bar.html', name="Breigh Ann")


@app.route('/dojos')
def dojo():
	return render_template('landing_page_dojos_bar.html', name="Breigh Ann")


app.run(debug=True)