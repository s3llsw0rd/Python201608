from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

app.secret_key = 'fortressOfSecurity'


@app.route('/')
def count():
    try: #check to see if user has an existing count session
        session['count']
    except:
    	session['count'] = 0
    session['count'] += 1
    return render_template('count_index.html')

@app.route('/reset', methods = ['POST'])
def reset():
	session['count'] = 0
	return redirect('/')

app.run(debug=True)