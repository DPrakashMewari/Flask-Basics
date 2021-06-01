import flask 
from flask import Flask,render_template
app = Flask(__name__)

# It is to show how other html we can extends  
# new inherit base feature

@app.route("/")
def home():
	return render_template("new.html",content="Pops")


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=1200,debug=True)