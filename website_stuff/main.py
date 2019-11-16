# -*- coding: utf-8 -*-
import os
import mysql.connector
import mysql.connector
import pymysql
from flask import Flask,render_template,request,session, jsonify, Response
import datetime
import pandas as pd
import json
import uuid
import hashlib
from datetime import date



## Connecting to the Google Cloud Database
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

global mypassword
global myEmail

app = Flask(__name__)
app.secret_key = "iloveyou3000"

def db_connection():
        db_user = os.environ.get('CLOUD_SQL_USERNAME')
        db_password = os.environ.get('CLOUD_SQL_PASSWORD')
        db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
        db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
        if os.environ.get('GAE_ENV') == 'standard':
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            cnx = pymysql.connect(user=db_user, password=db_password, unix_socket=unix_socket, db=db_name)
        else:
            host = '127.0.0.1'
            cnx = mysql.connector.connect(host="127.0.0.1", user = "root", password="root1234", database = "emp", unix_socket="/tmp/mysql.sock", auth_plugin="mysql_native_password")

        return cnx

@app.route('/about')
def about():
    cnx = db_connection()
    adminError = None
    myEmail = session.get('myEmail')
    # with cnx.cursor() as cursor:
    cursor = cnx.cursor()
    userCheck = cursor.execute('SELECT * FROM users WHERE email = %s', (myEmail,))
    entry = cursor.fetchall()
    
    num = list(entry)
    if len(num)==0:
        error = 'Invalid credentials'
        return render_template('login.html', error=error)
    else:
        myAdmin=0
        for element in num:
            if element[6]==1:
                myAdmin=1
                break
        error = None
    cnx.commit()
    cnx.close()

    return render_template('about.html', admin = myAdmin)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_index', methods=['GET', 'POST'])
def login_index():

    cnx = db_connection()
    adminError = None
    myEmail = request.form['email']
    mypassword = request.form['password']


    salt = hex(12)
    hashed_password = hashlib.sha512(mypassword.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    hpassword=str(hashed_password)


    print(myEmail)
    if session['myEmail']!=None:
        session['myEmail'] = myEmail
        session['mypassword'] = mypassword


    # with cnx.cursor() as cursor:
    cursor = cnx.cursor()
    userCheck = cursor.execute('SELECT * FROM users WHERE email = %s', (myEmail,))
    entry = cursor.fetchall()    

    num = list(entry)
    stored_pass=num[0][5]
    print(stored_pass)
    print(hpassword)

    if len(num)==0:
        error = 'No user with given email found.'
        return render_template('login.html', error=error)
    elif stored_pass!=hpassword:
        error = 'Invalid password entered.'
        return render_template('login.html', error=error)
    else:
        print("Authenticated!")
        myAdmin=0
        for element in num:
            if element[6]==1:
                myAdmin=1
                break
        error = None
    
    cnx.commit()

    hi = cursor.execute('SELECT * FROM emprewardz_transact_points as e join users as u on u.pk_user_id= e.source_user OR u.pk_user_id= e.dest_user where u.email = %s', (myEmail,))
    print(hi)

    dd = cursor.fetchall()
    print(dd)

    column = ["Giver","Receiver", "Points given","month", "month_id","Message"]
    list1 =[]
    for item in dd:
        hello = dict(zip(column, item))
        list1.append(hello.copy())
    df = pd.DataFrame(list1)
    cnx.close()
    return render_template("login_index.html", admin = myAdmin, tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

@app.route('/home', methods=['GET', 'POST'])
def home():
    cnx = db_connection()
    adminError = None
    myEmail = session.get('myEmail')


    # with cnx.cursor() as cursor:
    cursor = cnx.cursor()
    userCheck = cursor.execute('SELECT * FROM users WHERE email = %s', (myEmail,))
    entry = cursor.fetchall()
    
    num = list(entry)
    if len(num)==0:
        error = 'Invalid credentials'
        return render_template('login.html', error=error)
    else:
        print("Authenticated!")
        myAdmin=0
        for element in num:
            if element[6]==1:
                myAdmin=1
                break
        error = None
    
    cnx.commit()

    hi = cursor.execute('SELECT * FROM emprewardz_transact_points as e join users as u on u.pk_user_id= e.source_user OR u.pk_user_id= e.dest_user where u.email = %s', (myEmail,))
    print(hi)

    dd = cursor.fetchall()
    print(dd)

    column = ["Giver","Receiver", "Points given","month", "month_id","Message"]
    list1 =[]
    for item in dd:
        hello = dict(zip(column, item))
        list1.append(hello.copy())
    df = pd.DataFrame(list1)
    cnx.close()
    return render_template("home.html", admin = myAdmin, tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

## Add user - form 
@app.route('/adduser')
def main1():
    return render_template('user_form.html')

## Add user - submitted form 
@app.route('/usersubmitted', methods=['GET', 'POST'])
def usersubmitted():
    user_fname = request.form['fname']
    user_lname = request.form['lname']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    admin = request.form['admin']

    if len(password) == 0:
        return ("INVALID password. PLEASE TRY AGAIN!")
    else:
        # if os.environ.get('GAE_ENV') == 'standard':
        #     unix_socket = '/cloudsql/{}'.format(db_connection_name)
        #     cnx = pymysql.connect(user=db_user, password=db_password,
        #                           unix_socket=unix_socket, db=db_name)
        # else:
        #     host = '127.0.0.1'
        #     cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
        #     #cnx = mysql.connector.connect(host="127.0.0.1", user = "root", password="root1234", database = "emprewardz", unix_socket="/tmp/mysql.sock", auth_plugin="mysql_native_password")
        cnx=db_connection()

        cursor = cnx.cursor()

        myEmail = session.get('myEmail')
        print("THIS IS MY password", myEmail)

        salt = hex(12)
        hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        hpassword=str(hashed_password)

        userCheck = cursor.execute('SELECT * from users where email = %s', (myEmail,))
        entry = cursor.fetchall()
        print("THIS IS THE STUPID ENTRY", entry)
        print("THIS IS THE STUPID ENTRY", [x[6] for x in entry])

        tuplefromList = [x[6] for x in entry]
        adminCheck = tuplefromList[0]
        print(hpassword)
        if adminCheck == 1:
            cursor.execute('INSERT INTO users(user_fname, user_lname, phone, email, password, admin_status) VALUES (%s, %s, %s, %s, %s, %s)', (user_fname,user_lname, phone, email, hpassword, admin))

            hi = cursor.execute('SELECT pk_user_id from users where email = %s', (email,))
            entry = cursor.fetchall()
            print(entry)
            ID=entry[0][0]
            print(ID)

            hi = cursor.execute('SELECT max(month_id) from months')
            entry2 = cursor.fetchall()
            months=entry2[0][0]
            print(months)

            cursor.execute('INSERT INTO emprewardz_point_holder(user_id,points, month, month_id0) VALUES (%s, %s, %s, %s)',(ID,1000,date.today(),months))
            cnx.commit()
            cnx.close()
            adminError = None
        else:  
            adminError = 'You are not allowed to perform this action!'
            return render_template('login_index.html', adminError=adminError)
    
    return render_template('user_submitted_form.html', user_fname=user_fname, user_lname=user_lname,email=email, phone=phone, password=password,admin=admin)

@app.route('/deleteuser')
def deletemain():
    return render_template('delete_user_form.html')

## Add user - submitted form 
@app.route('/userdeleted', methods=['GET', 'POST'])
def deleted_form():
    email = request.form['email']

    myEmail = session.get('myEmail')
    #print("THIS IS MY password", myEmail)

    cnx=db_connection()
    cursor = cnx.cursor()

    userCheck = cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    entry = cursor.fetchall()
    
    num = list(entry)
    if len(num)==0:
        error = 'Invalid credentials'
        return render_template('delete_user_form.html', error=error)
    else:
        
        myEmail = session.get('myEmail')
        print("THIS IS MY password", myEmail)

        userCheck = cursor.execute('SELECT * from users where email = %s', (myEmail,))
        entry = cursor.fetchall()
   

        tuplefromList = [x[6] for x in entry]
        adminCheck = tuplefromList[0]
        
        if adminCheck == 1:
            cursor.execute('DELETE FROM users WHERE email = %s', (email,))
            cnx.commit()
            adminError = None
        else:  
            adminError = 'You are not allowed to perform this action!'
            return render_template('login_index.html', adminError=adminError)
    return render_template('user_deleted_form.html', email=email)


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
    print(dd)
    column = ["pk_user_id", "user_fname","user_lname", "phone", "email", "password", "admin"]
    list =[]
    
    for item in dd:
        hello = dict(zip(column, item))
        list.append(hello.copy())
    jusers = json.dumps(list).replace("null","empty")
    #jusers = jsonify(list)
    print(jusers)

    return Response(jusers, mimetype='application/json')

@app.route('/aggregatePoints')
def main3():
    cnx=db_connection()
    cursor = cnx.cursor()    
    df = pd.read_sql_query("SELECT * FROM agg_points", cnx)
    return render_template('agg_points_report.html', tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

@app.route('/report2')
def report2():
    return ('x')

@app.route('/report3')
def report3():
    cnx=db_connection()
    cursor = cnx.cursor()    
    df = pd.read_sql_query("SELECT A.user_id, A.month_id2, A.PointsRedeemed FROM agg_points as A", cnx)
    return render_template('redeem_points_report.html', tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

@app.route('/givePoints')
def main4():
    cnx=db_connection()
    cursor = cnx.cursor() 
    myEmail = session.get('myEmail')
    #df= pd.read_sql_query('SELECT * FROM emprewardz_point_holder join users on pk_user_id=user_id where email = %s', (myEmail,),cnx)
    hi = cursor.execute('SELECT e.user_id,e.total,e.points,e.month,e.month_id0 FROM emprewardz_point_holder as e join users as u on u.pk_user_id= e.user_id where u.email = %s', (myEmail,))
    print(hi)

    dd = cursor.fetchall()
    print(dd)

    column = ["user_id","My total points", "Points to give","month", "month_id"]
    list =[]
    for item in dd:
        hello = dict(zip(column, item))
        list.append(hello.copy())
    df = pd.DataFrame(list)
    print(list)
    return render_template('give_points.html', tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

@app.route('/pointsGiven', methods=['GET', 'POST'])
def pointsGiven():
    user_fname = request.form['user_fname']
    user_lname = request.form['user_lname']
    email = request.form['email']
    points = request.form['points']
    comment = request.form['comment']

    myEmail = session.get('myEmail')

    cnx=db_connection()
    cursor = cnx.cursor()    

    you = cursor.execute('SELECT e.user_id FROM emprewardz_point_holder as e join users as u on u.pk_user_id= e.user_id where u.email = %s', (myEmail,))
    print(you)
    entry1 = cursor.fetchall()
    print(entry1)

    pointsToGive = cursor.execute('SELECT e.points FROM emprewardz_point_holder as e join users as u on u.pk_user_id= e.user_id where u.email = %s ORDER BY e.month_id0 DESC LIMIT 1', (myEmail,))
    print(pointsToGive)
    entry2 = cursor.fetchall()
    print(entry2)

    recieve = cursor.execute('SELECT e.user_id FROM emprewardz_point_holder as e join users as u on u.pk_user_id= e.user_id where u.email = %s', (email,))
    print(recieve)
    entry3 = cursor.fetchall()
    print(entry3)

    month = cursor.execute('SELECT max(month_id) from months')
    print(recieve)
    entry4 = cursor.fetchall()
    print(entry4)

    yous = entry1[0][0]
    pointsToGiven = (entry2[0])
    reciever = entry3[0][0]
    months= entry4[0][0]

    print(yous,reciever,points,months)

    if int(points)< int(pointsToGiven[0]):
        cursor.callproc('stored_proc',(yous,reciever,points,months,comment))
        cnx.commit()

    else:
        raise Exception('Error: You Connot send more points than you currently have!')

    cnx.close()
    return render_template('give_points.html')

@app.route('/redeemPoints')
def redeem():
    return('x')

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='localhost', debug=True)



