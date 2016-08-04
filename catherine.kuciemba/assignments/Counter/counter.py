from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def count():
    try:
        session['count']
    except:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')
app.run(debug=True)
