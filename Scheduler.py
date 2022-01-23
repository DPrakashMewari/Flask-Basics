from flask import Flask 
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


app  = Flask(__name__)
scheduler = BlockingScheduler()
scheduler.start()

def home():
    print("I will be Display in every 5 second")


# This Scheduler will help based on Daily Month Yearly or Hour Seconds ,week 
@app.route("/")
def hello_1():
    simple1 = {3:[{'seconds':'5','start_time':'2020-1-20 16:45:00','end_time':'2020-1-20 16:46:00'}]}
    for i in simple1[3]:
        print("*")
        if i['seconds'] == '5':
            job=scheduler.add_job(id='Scheduler 1',trigger='interval',start_date=i['start_time'],end_date=i['end_time'])
                
    return simple1



if __name__ == "__main__":
    # scheduler.add_job(id="Scheduler task",func=hello,trigger='cron',day="1-29",start_date=datetime.now(),end_date='2022-1-20 13:22:00')
    app.run()