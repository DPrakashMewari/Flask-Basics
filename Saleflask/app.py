from flask import Flask, request, flash, url_for, redirect, render_template
import con
from con import *


class New(db.Model):
    id = db.Column('Product_id', db.Integer, primary_key=True)
    Product = db.Column(db.String(100))
    Qty = db.Column(db.Float(50))
    Price = db.Column(db.Integer)


    def __init__(self, Product, Qty, Price):
        self.Product = Product
        self.Qty = Qty
        self.Price = Price



@app.route('/')
def list_employees():
    return render_template('list_employees.html', Employees=New.query.all())


@app.route('/add', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST':
        if not request.form['Product'] or not request.form['Qty'] or not request.form['Price']:
            flash('Please enter all the fields', 'error')
        else:
            employee = New(request.form['Product'], request.form['Qty'],request.form['Price'])

            db.session.add(employee)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('list_employees'))
    return render_template('add.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)