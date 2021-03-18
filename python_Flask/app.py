from flask import Flask, session
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
    )

app.secret_key = b'p83129'

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/signin", methods=["POST"])
def signin():
    x=request.form["number1"]
    y=request.form["number2"]
   
    if x == "test" and y == "test":
        session['sucess'] = '已登入'  
        print(session['sucess'])      
        return redirect(url_for('member'))
    else:
        return redirect(url_for('error'))

@app.route("/member")
def member():       
    if session['sucess'] == '已登入':
        return render_template("member.html")
    else:
        return redirect(url_for('index'))

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/signout")
def aaa():
    session['sucess'] = '未登入'  
    print(session['sucess'])  
    return redirect(url_for('index'))
    
        

app.run(port=3000)    
