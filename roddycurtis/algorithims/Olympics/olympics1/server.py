from flask import Flask, render_template 
app = Flask(__name__)
# app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

  app.run(debug = True)
