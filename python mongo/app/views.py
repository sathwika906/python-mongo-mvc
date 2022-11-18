
from app import app
from flask import Flask, render_template, redirect, request



#@app.route('/', methods=['GET',"POST"])
#def reg():
 #   return render_template('registration.html')
    
@app.route('/')
def index():
    # if request.method=='POST':
        return render_template('initial.html')
@app.route('/signuppage')
def signuppage():
    return render_template('signup.html')
@app.route('/searchpage')
def searchpage():
    return render_template('searchpage.html')



@app.route('/link')
def link():
    return render_template('link.html')


@app.route('/table')
def table():
    return render_template('table.html')



@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

