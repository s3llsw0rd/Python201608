from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key ='secret'


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    data= request.form
    error =False
    if len(request.form['name']) < 1:
        session['name_len'] = "Please enter a name"
        error=True
    if len(request.form['comment']) <1:
        session['comment_len'] ="Please enter a comment"
        error=True
    if len(request.form['comment']) >120:
        session['comment_len']="You can only enter up to 120 characters"
        error=True
    if error:
        return redirect('/')
    session.pop('name_len')
    session.pop('comment_len')



    name= request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("results.html", name=name, location=location, language=language, comment=comment)
   # return redirect('results.html' )
app.run(debug=True)
