from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import re

PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<arg>')
def ninja(arg):
    print arg
    return render_template("index.html", arg=arg)

@app.route('/ninja/<path:arg>')
def color(arg):
    turtles = {
        # 'red': "raphael",
        'red': "raphael",
        'blue': 'leonardo',
        'purple': 'donatello',
        'orange': 'michelangelo'
    }
    if arg not in ['red', 'blue', 'purple', 'orange']:
        arg = 'april'
    return render_template("index.html", arg=arg)


# @app.route('/process', methods=['POST'])
# def process():
#     return redirect("/")

app.run(debug=True) # run our servers
