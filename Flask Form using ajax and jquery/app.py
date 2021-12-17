from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('form.html')

@app.route("/signup",methods=['POST'])
def signup():
    user = request.form['username']
    password = request.form['password']
    return json.dumps({'status':'ok','user':user,'pass':password})
if __name__ == "__main__":
    app.run(debug=True)
