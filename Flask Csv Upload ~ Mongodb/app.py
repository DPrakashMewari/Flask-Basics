from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt 
import conn 
from conn import *

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', shape=df.shape,tables=[df.head(5).to_html(classes='data', header="true")],info=df.describe().to_html(classes='data', header="true"))
    return render_template('upload.html')

@app.route("/cloud",methods=['GET', 'POST'])
def uploadtocloud():
    if request.method == 'POST':
        db = client.test
        employee = db.employee 
        df = pd.read_csv(request.files.get('file'))
        records_ = df.to_dict(orient = 'records') 
        result = db.employee.insert_many(records_ ) 
        return "Record Inserted Successfully"
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)


