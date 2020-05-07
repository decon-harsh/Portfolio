#imports
from Profile import app,db,bcrypt
from flask import redirect,render_template,url_for,flash,request
from flask import render_template,url_for,flash,redirect,request

#Routes
@app.route('/',methods=['GET','POST'])
def Main():
    return render_template('Welcome_Page.html',title="Welcome to my profile")

@app.route('/basic_details',methods=['GET','POST'])
def Basic_Details():
    return render_template('Basic_Details.html',title="Basic_Details")

@app.route('/education',methods=['GET','POST'])
def Education():
    return render_template('Education.html',title="Educational Details")

@app.route('/project',methods=['GET','POST'])
def Projects():
    return render_template('Projects.html',title="Projects")

@app.route('/hobbies',methods=['GET','POST'])
def Hobbies():
    return render_template('Hobbies.html',title="Hobbies")
