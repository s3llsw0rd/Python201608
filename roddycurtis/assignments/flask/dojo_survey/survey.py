from flask import Flask, render_template, request, redirect
                                       
app = Flask(__name__)                    
                                          
@app.route('/')                           
def homepage():
	return render_template("surveyhome.html") 
@app.route('/route.html',methods=['POST']) 
def create():
    data = request.form
    print data
    return render_template('route.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)