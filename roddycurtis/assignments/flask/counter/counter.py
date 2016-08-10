from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def counter():
    try:
        session['counter']
    except:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('counter.html')

if __name__ == '__main__':
  app.run(debug = True)