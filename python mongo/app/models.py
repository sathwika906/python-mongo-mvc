from app import app
from flask import render_template
from flask import Flask, redirect, url_for, render_template, request, session
import pymongo
from cgitb import html
from pymongo import MongoClient 
#import random
from random import randint

# app = Flask(__name__, template_folder='templates')
try:
    client = MongoClient("mongodb://localhost:27017")
    db = client['mongomvc1']
    Collection = db["Patient12"]
    # client.server_info() #trigger exception if it cannot connect to database
    
except Exception as e:
    print(e)
    print("Error - Cannot connect to database")
l=list()
firstname = " "
add = 0
res = " "
patientid = " "
@app.context_processor
def context_processor():
    # if we directly return the value then its showing not definedName=pname,Email=pemail,Gender=pgender,Dob=pdob,PIN=ppin
    return dict(lo=l)

@app.route('/signup', methods=['GET',"POST"])
def signup():
    global patientid
    global firstname
    # middlename=""
    lastname = " "
    gender = " "
    email=""
    birthday = " "
    pin = " "
    pno=""
    adhar=""
    #patient_id=0
    patientid = randint(10000000000000,99999999999999)
    print(patientid)
    if request.method == "POST":
    
        firstname = request.form['firstname']
        # middlename=request.form['middlename']
        lastname = request.form['lastname']
        gender = request.form['gender']
        email=request.form['email']
        birthday = request.form['birthday']
        pin = request.form["pincode"]
        adhar=request.form['adhar']
        pno=request.form['pno']
      #  patient_id=randompatient_id(14)
        
        Collection.insert_one(
             {"patientid":patientid,
        "fname" : firstname,
        "lastname":lastname,
        # "middlename":middlename,
        "gender":gender,
        "email":email,
        "birthday":birthday,
        "pin":pin, 
        "pno":pno,
        "adhar":adhar
        }
        )
        k=firstname
        k=k+lastname
    return render_template('table.html',id = patientid ,nm=k)

@app.route('/submit', methods=['GET',"POST"])
def submit():
    
    if request.method == "POST":
        print("this is table page ")
        while True:
            p1 = request.form.get('age')
            p2 = request.form.get('2pp')
            p3 = request.form.get('3pp')
            p4 = request.form.get('4pp')
            p5 = request.form.get('5pp')
            p6 = request.form.get('6pp')
            Collection.update_one(
                {"firstname":firstname},
            {"$set": {"p1" :p1,
            'p2': p2,
             "p3":p3,
            "p4":p4,
            "p5":p5,
            "p6":p6}}
        
        )

            print(f"this is table value {p1}-{p2}-{p3}-{p4}-{p5}-{p6}")
            score = int(p1)+int(p2)+int(p3)+int(p4)+int(p5)+int(p6)
            global add
            add=score  
            global res
            if score > 4 :
                res="screening needed"
                Collection.update_one(
                {"firstname":firstname},
                {"$set": {"total_count" :add}})
            else:
                res="no need to screen"
                Collection.update_one(
                #{"firstname":firstname},{"$set": {"total_count" :add}})
                 {"id" :patientid,},{"$set": {"total_count" :add,"res" :res}})
            return render_template('result.html', sc=score,result=res)
    return render_template('signup.html')

@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('initial.html')


# if __name__ == "__main__":
#      try:
#         client = MongoClient("mongodb://localhost:27017")
#         db = client['mongomvc1']
#         Collection = db["Patient12"]
#         # client.server_info() #trigger exception if it cannot connect to database
        
#      except Exception as e:
#         print(e)
#         print("Error - Cannot connect to database")
#      app.run(debug=True)