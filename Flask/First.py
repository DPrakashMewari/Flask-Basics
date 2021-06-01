import flask 
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello This is Prakash"
@app.route("/<name>")
def home1(name):
	return f"Hello This is {name} Prakash!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8000)