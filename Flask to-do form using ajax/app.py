from flask import *
import pyodbc


app = Flask(__name__)
# Connection url
connection = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-S9E8538\SQLEXPRESS;Database=Prakash;uid=root;pwd=root@123')    



@app.route("/")
def home():
    return render_template('form.html')

@app.route("/eventsubmit",methods=['POST'])
def eventsubmit():
    title = request.form['title']
    desc = request.form['description']
    start = request.form['start']
    end = request.form['end']
    place = request.form['place']
    lat = request.form['lat']
    long_ = request.form['long']
    cursor = connection.cursor()    
    SQLCommand = ("INSERT INTO dbo.event_tbl(title, description, start,endd,place,lat,long) VALUES (?,?,?,?,?,?,?)")    
    values = [title,desc,start,end,place,lat,long_]
    cursor.execute(SQLCommand,values)
    connection.commit()
    print('Data Inserted')
    return json.dumps({'status':'ok','title':title,'desc':desc,'start':start,'end':end,'place':place,'lat':lat,'long':long_})


if __name__ == "__main__":
    app.run(debug=True)
