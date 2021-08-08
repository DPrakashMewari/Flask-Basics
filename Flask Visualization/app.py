import flask 
from flask import Flask,render_template,request,url_for
import pandas as pd 

app = Flask(__name__)


@app.route("/")
def index():
	data = [
		('01-01-2020',1597),
		('02-03-2020',141),
		('03-01-2020',254),
		('04-01-2020',2541),
		('05-01-2020',2543),
		('06-01-2020',222),
		('07-01-2020',211),
		  ]
	labels = [row[0] for row in data]
	values = [row[1] for row in data]
	return render_template('chart.html',labels=labels,values=values)

@app.route("/barplot")
def barplot():
	data = [ 
		('Sunday',22),
		('Monday',100),
		('Tuesday',33),
		('Wednesday',42),
		('Thursday',43),
		('Friday',231),
		('Saturday',21),
	]

	day = [row[0] for row in data]
	point = [row[1] for row in data]

	return render_template("bar.html",labels=day,values=point)




if __name__ == '__main__':
	app.run(debug=True)