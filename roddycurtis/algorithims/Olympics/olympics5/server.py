from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['GET'])
def process():
   
    return ('I love flask')


if __name__ == '__main__':
  app.run(debug = True)


"""
Will this work?  What
What will this print???
"""
