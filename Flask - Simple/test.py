import flask 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return """


	<h1>Hello</h1>
 	<h4> Prakash </h4>
 	"""

if __name__ == "__main__":
	app.run(debug=True)