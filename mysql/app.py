import flask
from flask import Flask,request,render_template,redirect,flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret_key"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="prakash1"
)



@app.route("/create")
def create():
	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
	return "Table created"

@app.route("/",methods=['POST','GET'])
def insert():
	mycursor = mydb.cursor()
	if request.method == "POST":
		name = request.form['name']
		address = request.form['address']
		sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
		val = (name,address)
		mycursor.execute(sql,val)
		mydb.commit()
		flash("Record Inserted")
		return redirect("/")
	else:
		return render_template("add.html")
@app.route("/delete")
def delete():
	mycursor = mydb.cursor()
	sql = "delete from customers where address = 'dd'"
	mycursor.execute(sql)
	mydb.commit()
	flash("Record Deleted")
	return redirect("/")
@app.route("/update")
def update():
	mycursor = mydb.cursor()
	sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'dede'"
	mycursor.execute(sql)
	mydb.commit()
	flash("Record updated")
	return redirect("/")
@app.route("/show")
def show():
	mycursor = mydb.cursor()
	mycursor.execute("Select * from customers")
	myresult = mycursor.fetchall()
	for x in enumerate(myresult):
		flash(x)
	return redirect("/")






	
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=1200,debug=True)


