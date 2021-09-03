from flask import Flask, request, flash, url_for, redirect, render_template
from con import *

mail = Mail(app)

class New(db.Model):
    id = db.Column('Product_id', db.Integer, primary_key=True)
    Product = db.Column(db.String(100))
    barcode = db.Column(db.String(50))
    Stock = db.Column(db.Float(50))
    Price = db.Column(db.Integer)

    def __init__(self,Product,barcode,Stock,Price):
        self.Product = Product
        self.barcode= barcode
        self.Stock = Stock
        self.Price = Price




@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/prod")
def productpage():
    return render_template('Products.html',Product=New.query.all())

@app.route('/addproduct', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        Product = request.form['Product']
        barcode = request.form['barcode']
        Stock = request.form['Stock']
        Price = request.form['Price']
        data = New(Product=Product,barcode=barcode,Stock=Stock,Price=Price)
        db.session.add(data)
        db.session.commit()
        flash("Stock Updated")
        return redirect(url_for('homepage'))
    return render_template('Products.html')

@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = New.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    msg = Message('subject', sender='Prakash.mewari@gmail.com', recipients=['Prakash.mewari@gmail.com'])
    flash("Product Sell.Also Please Check You Mail")
    msg.body = "Product Successfully Sell by Admin"
    mail.send(msg)



    return redirect(url_for('productpage'))





if __name__ == "__main__":
    db.create_all()
    app.run(debug=True,port=4000)