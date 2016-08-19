from flask import Flask, request, render_template, session, redirect, Markup
import random 
app = Flask(__name__)
app.secret_key = "secretshhh"

@app.route('/')
def main():    
    if "gold" not in session:
        session["gold"] =  0
        session['activities']=""
    return render_template('index.html')

@app.route('/process_money', methods = ["post"])
def money():
    if request.form['place'] == "farm":
        gold = random.randint(10,20)        
        session['gold']+=gold
        session['activities']+=Markup("<p>earned {} gold from the farm</p>".format(gold))
        return redirect("/")
    elif request.form['place'] == "cave":
        gold = random.randint(5,10)
        session['gold']+=gold
        session['activities']+=Markup("<p>earned {} gold from the cave</p>".format(gold))
        return redirect("/")
    elif request.form['place'] == "house":
        gold = random.randint(2,5)
        session['gold']+=gold
        session['activities']+=Markup("<p>earned {} gold from the house</p>".format(gold))
        return redirect("/")
    elif request.form['place'] == "casino":
        gold = random.randint(-50,50)
        session['gold']+=gold
        if gold > 0:
            session['activities']+=Markup("<p>entered a casino and made {} gold</p>".format(gold))
        else:
            session['activities']+=Markup("<p class= 'red'>entered a casino and lost {} gold..Ouch</p>".format(gold*-1))
        return redirect("/")



app.run(debug=True)    
