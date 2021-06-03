# it is about session 
import flask 
from flask import Flask,render_template,url_for,request,session,redirect
import datetime 
from datetime import timedelta

app = Flask(__name__)
app.secret_key  = "secret_key"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
	return render_template("new.html")

@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == "POST":
		session.permanent = True
		name = request.form['name']
		session['name'] = name 
		return redirect(url_for("user"))
	else:
		if "user" in session:
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user")
def user():
	if "name" in session:
		name = session['name']
		return f"</h1>{name}</h1>"
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user",None)
	return redirect(url_for("login"))


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=1100,debug=True)