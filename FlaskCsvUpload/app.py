from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt 

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', shape=df.shape,tables=[df.head(5).to_html(classes='data', header="true")],info=df.describe().to_html(classes='data', header="true"))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)