from flask import Flask, render_template, request, redirect, url_for, session, flash
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    return render_template("result.html")


@app.route('/process', methods=['POST'])
def process():
    formInfo = {    'name': request.form['name'],
                    'location': request.form['location'],
                    'lang': request.form['lang'],
                    'comment': request.form['comment']
                }
    session['values'] = formInfo
    print session['values']['location']

    for val in formInfo.items():
        if len(val[1]) < 1:
            string = val[0] + ' cannot be empty!'
            flash(string)
    if len(formInfo['comment']) > 120:
        flash("Comment needs to be under 120 characters")
    return redirect("/result")

app.run(debug=True) # run our servers
