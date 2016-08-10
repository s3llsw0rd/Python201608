from flask import Flask, render_template  
                                         
app = Flask(__name__)                    
                                          
@app.route('/')                           
def hello_world():
  return render_template('index.html')   
@app.route('/ninjas')
def success():
  return render_template('ninjas') 
 @app.route('/dojos/new')
def success():
  return render_template('newdojo') 
app.run(debug=True)