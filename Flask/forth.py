import flask 
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


# GET : SEND A DATA  {IT IS NOT PROTECTIVE}
# POST : SEND A DATA  {IT IS Protective and encryptes when sending data}

@app.route("/",methods=['POST',"GET"])
def login():
	# Give condition if post then redirect to my user api
	if request.method =="POST":
		user = request.form['name']
		surname = request.form['surname']
		return redirect(url_for("user",usr=surname))
	# else you will get back to base login 	
	else:
		return render_template("login.html")
# Function to Display a name when we pass name in a html 
@app.route("/<usr>")
def user(usr):
	return f"<h1>{usr}</h1>"


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=1200,debug=True)