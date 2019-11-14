# -*- coding: utf-8 -*-
import os
import mysql.connector
import mysql.connector
import pymysql
from flask import Flask,render_template,request,session, jsonify, Response
import datetime
import pandas as pd
import json


## Connecting to the Google Cloud Database
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

global mypassword

app = Flask(__name__)
app.secret_key = "iloveyou3000"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_index', methods=['GET', 'POST'])
def login_index():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
    adminError = None
    myEmail = request.form['email']
    mypassword = request.form['password']

    session['mypassword'] = mypassword

    # with cnx.cursor() as cursor:
    cursor = cnx.cursor()
    userCheck = cursor.execute('SELECT * FROM users WHERE password = %s AND email = %s', (mypassword, myEmail))
    entry = cursor.fetchall()
    
    num = list(entry)
    if len(num)==0:
        error = 'Invalid credentials'
        return render_template('login.html', error=error)
    else:
        myAdmin=0
        for element in num:
            if element[5]==1:
                myAdmin=1
                break
        error = None
    
    cnx.commit()
    cnx.close()

    return render_template("login_index.html", admin = myAdmin)

## Add user - form 
@app.route('/adduser')
def main1():
    return render_template('user_form.html')

## Add user - submitted form 
@app.route('/usersubmitted', methods=['GET', 'POST'])
def usersubmitted():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    admin = request.form['admin']

    if len(password) != 7:
        return ("INVALID password. PLEASE TRY AGAIN!")
    else:
        if os.environ.get('GAE_ENV') == 'standard':
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            cnx = pymysql.connect(user=db_user, password=db_password,
                                  unix_socket=unix_socket, db=db_name)
        else:
            host = '127.0.0.1'
            cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
        cursor = cnx.cursor()

        mypassword = session.get('mypassword')
        print("THIS IS MY password", mypassword)

        userCheck = cursor.execute('SELECT * from users where password = %s', (mypassword,))
        entry = cursor.fetchall()
        print("THIS IS THE STUPID ENTRY", entry)
        print("THIS IS THE STUPID ENTRY", [x[5] for x in entry])

        tuplefromList = [x[5] for x in entry]
        adminCheck = tuplefromList[0]
        
        if adminCheck == 1:
            cursor.execute('INSERT INTO users(user_fname, user_lname, phone, email, password, admin) VALUES (%s, %s, %s, %s, %s)', (user_fname,user_lname, phone, email, password, admin))
            cnx.commit()
            cnx.close()
            adminError = None
        else:  
            adminError = 'You are not allowed to perform this action!'
            return render_template('login_index.html', adminError=adminError)
    
    return render_template('usersubmitted.html', user_fname=user_fname, user_lname=user_lname,email=email, phone=phone, password=password,admin=admin)
 
@app.route('/deleteuser')
def deletemain():
    return render_template('delete_user_form.html')

## Add user - submitted form 
@app.route('/userdeleted', methods=['GET', 'POST'])
def deleted_form():
    email = request.form['email']
    password = request.form['password']

    mypassword = session.get('mypassword')
    print("THIS IS MY password", mypassword)

    if len(password) != 7:
        return ("INVALID password. PLEASE TRY AGAIN!")
    else:
        
        if os.environ.get('GAE_ENV') == 'standard':
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            cnx = pymysql.connect(user=db_user, password=db_password,
                                  unix_socket=unix_socket, db=db_name)
        else:
            host = '127.0.0.1'
            cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
       
        cursor = cnx.cursor()

        userCheck = cursor.execute('SELECT * FROM users WHERE password = %s AND email = %s', (password, email))
        entry = cursor.fetchall()
        
        num = list(entry)
        if len(num)==0:
            error = 'Invalid credentials'
            return render_template('delete_user_form.html', error=error)
        else:
            
            mypassword = session.get('mypassword')
            print("THIS IS MY password", mypassword)

            userCheck = cursor.execute('SELECT * from users where password = %s', (mypassword,))
            entry = cursor.fetchall()
       

            tuplefromList = [x[5] for x in entry]
            adminCheck = tuplefromList[0]
            
            if adminCheck == 1:
                cursor.execute('DELETE FROM users WHERE password = %s', (password,))
                cnx.commit()
                adminError = None
            else:  
                adminError = 'You are not allowed to perform this action!'
                return render_template('login_index.html', adminError=adminError)
        return render_template('user_deleted_form.html', email=email,password=password)


@app.route('/usertable', methods=['GET', 'POST'])
def usertable():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                               unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
   
    cursor = cnx.cursor() 
    result = cursor.execute("Select * from users")
    dd = cursor.fetchall()
    column = ["pk_user_id", "user_fname","user_lname", "phone", "email", "password", "admin"]
    list =[]
    
    for item in dd:
        hello = dict(zip(column, item))
        list.append(hello.copy())
    
    jusers = json.dumps(list).replace("null","empty")
    #jusers = jsonify(list)
    print(jusers)

    return Response(jusers, mimetype='application/json')


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='localhost', debug=True)
