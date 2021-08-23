from flask import Flask, request, render_template,send_file
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', shape=df.shape,tables=[df.head(5).to_html(classes='data', header="true")],info=df.describe().to_html(classes='data', header="true"))
    return render_template('upload.html')



@app.route("/plot",methods=['POST','GET'])
def dplot():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        categoricalcol = [x for x in df.dtypes.index if df.dtypes[x]=='object']
        numericaltypecol = [x for x in df.dtypes.index if df.dtypes[x]=='int64']
        floattypecol = [x for x in df.dtypes.index if df.dtypes[x]=='float64']
        fig = go.Figure()
        for col in categoricalcol:
            fig = px.bar(df, x=df[col], y=df.index)
            print(categoricalcol)
            fig.show()
        return render_template('index.html',name=fig.show)
    return render_template('upload.html')




if __name__ == '__main__':
    app.run(debug=True)


