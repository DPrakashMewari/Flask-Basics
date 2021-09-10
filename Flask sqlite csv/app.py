from flask import Flask, request, render_template, send_file
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)

app = Flask(__name__)


@app.route("/")
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        df.to_sql('file', con=engine)
        var = engine.execute("SELECT * FROM file limit 5").fetchall()
        df = pd.read_sql('file', engine)
        return render_template('upload.html', shape=df.shape,
                               tables=[df.head(5).to_html(classes='data', header="true")],
                               info=df.describe().to_html(classes='data', header="true"),
                               sql1=var)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
