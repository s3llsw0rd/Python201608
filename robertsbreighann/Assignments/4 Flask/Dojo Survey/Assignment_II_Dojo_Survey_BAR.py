from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('Assignment II Dojo Survey_BAR.html')

@app.route('/create', methods = ['POST'])
def create():
    data = request.form
    print data
    return render_template('Assignment II Dojo Survey_result_BAR.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)