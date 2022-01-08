from Flask_form import app,flow,GOOGLE_CLIENT_ID
from flask import render_template,redirect,url_for,flash,session,request,abort
from Flask_form.forms import RegisterForm,LoginForm
from Flask_form import connection

import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests


# def login_is_required(function):
#     def wrapper(*args, **kwargs):
#         if "id" not in session:
#             return abort(401)  # Authorization required
#         else:
#             return function()

#     return wrapper


@app.route("/googlelogin")
def googlelogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["id"] = id_info.get("sub")
    session["username"] = id_info.get("name")
    return redirect(url_for("dashboard"))



@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    username = form.username.data
    password = form.password.data        
    cursor = connection.cursor()
    cursor.execute('Select * from dbo.user1 where username = ? and password = ?',(username,password,))
    print("Query complete")
    user1 = cursor.fetchone()
    if user1:
        session['loggedin'] = True
        session['id'] = int(user1.id)
        session['username'] = str(user1.username)
        print("Logged")
        flash(f"Success ! You are Logged ",category='success')
        return redirect(url_for('dashboard'))  
    elif user1:
        session['loggedin'] = False     
        flash(f"Fail ! You are not Logged Wrong User name Pass ",category='danger')        
    return render_template('login.html',form=form)


@app.route("/protectedarea")
def dashboard():
    return render_template('dashboard.html')

@app.route('/Register',methods=['POST','GET'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        emailaddress = form.email_address.data
        password = form.password1.data
        cursor = connection.cursor()
        SQLCommand = ("INSERT INTO dbo.user1(username, emailaddress, password) VALUES (?,?,?)")    
        values = [username,emailaddress,password]
        cursor.execute(SQLCommand,values)
        print("Data Inserted")
        connection.commit()
        return redirect("/")
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with creating  a user: {err_msg}",category='danger')
    return render_template('register.html',form=form)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/crud")
def crud():
    return render_template("crud.html")