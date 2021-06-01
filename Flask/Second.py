import flask 
from flask import Flask,url_for,redirect,render_template

app = Flask(__name__)


@app.route("/<name>")
def home(name):
	return render_template("index.html",content=['Prakash','aysh','DSFS','dd'])



@app.route("/<name>")
def user(name):
	return f"Hello This is {name} Prakash"


@app.route("/vendor/")
def admin():
	return redirect(url_for("user",name="Admin!"))


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=1100)