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
global myEmail

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

    session['myEmail'] = myEmail
    session['mypassword'] = myEmail


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

        myEmail = session.get('myEmail')
        print("THIS IS MY password", myEmail)

        userCheck = cursor.execute('SELECT * from users where email = %s', (myEmail,))
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

    myEmail = session.get('myEmail')
    #print("THIS IS MY password", myEmail)

    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
   
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
   

        tuplefromList = [x[5] for x in entry]
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
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
    cursor = cnx.cursor()    
    df = pd.read_sql_query("SELECT * FROM agg_points", cnx)
    return render_template('agg_points_report.html', tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

@app.route('/givePoints')
def main4():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
    cursor = cnx.cursor() 
    myEmail = session.get('myEmail')
    #df= pd.read_sql_query('SELECT * FROM emprewardz_point_holder join users on pk_user_id=user_id where email = %s', (myEmail,),cnx)
    hi = cursor.execute('SELECT e.user_id,e.points,e.month,e.month_id FROM emprewardz_point_holder as e join users as u on u.pk_user_id= e.user_id where u.email = %s', (myEmail,))
    print(hi)

    dd = cursor.fetchall()
    print(dd)

    column = ["user_id", "points","month", "month_id"]
    list =[]
    for item in dd:
        hello = dict(zip(column, item))
        list.append(hello.copy())
    df = pd.DataFrame(list)
    print(list)
    return render_template('give_points.html', tables=[df.to_html(classes='data', index=False, header="true")], titles=df.columns.values )

@app.route('/pointsGiven', methods=['GET', 'POST'])
def eventsubmitted():
    return ("x")
if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='localhost', debug=True)

#     name = request.form['name']
#     description = request.form['description']
#     expected_attendance = request.form['expected-attendance']
#     venue_id = request.form['venue_id']
#     event_owner = request.form['event_owner']
#     start_time = request.form['start_time']

#     print(name, description, venue_id, event_owner, start_time)

#     if os.environ.get('GAE_ENV') == 'standard':
#         unix_socket = '/cloudsql/{}'.format(db_connection_name)
#         cnx = pymysql.connect(user=db_user, password=db_password,
#                               unix_socket=unix_socket, db=db_name)
#     else:
#         host = '127.0.0.1'
#         cnx = mysql.connector.connect(host="127.0.0.1", user = "root", database = "test", unix_socket="C:/xampp/mysql/mysql.sock")
#     cursor = cnx.cursor()    
#     infoGrab = cursor.execute('SELECT * FROM venues WHERE venue_id = %s', (venue_id,))
#     entry = cursor.fetchall()

#     print("THIS IS ENTRY", entry)

#     tuplefromList = [x[4] for x in entry]
#     venueAttendance = int(tuplefromList[0])

#     print(tuplefromList)
#     print("VENUE ATTENDANCE:", venueAttendance)
            

#     if int(expected_attendance) < venueAttendance:  
#         venueCheck = cursor.execute('SELECT * FROM Time WHERE venue_id = %s AND timeslot = %s', (venue_id, start_time,))
#         timeEntry = cursor.fetchall()
#         tuplefromTimeEntry = [x[1] for x in timeEntry]

#         if tuplefromTimeEntry[0] is None: 
#             sql = "INSERT INTO events(name, description, expected_attendance, venue_id, event_owner, start_time) VALUES (%s, %s, %s, %s, %s, %s)"
#             cursor.execute(sql, (name, description, expected_attendance, venue_id, event_owner, start_time))
   
#             eventID = cursor.lastrowid

#             ## UPDATES THE TIME TABLE
#             updateTime = "UPDATE Time SET event_id = %s WHERE timeslot = %s and venue_id = %s "
#             cursor.execute(updateTime,(eventID, start_time, venue_id))

#             ## INSERT JOIN
#             cursor.execute('SELECT * FROM users WHERE EID = %s', (event_owner,))
#             row = cursor.fetchall()

#             tuplefromID = [x[0] for x in row]
#             userID = tuplefromID[0]

#             insertJoin = "INSERT INTO confirmedEvents(event_id, user_id) VALUES (%s, %s)" 
#             cursor.execute(insertJoin, (eventID, userID))

#             ## MODIFIES THE CURRENT ATTENDANCE
#             updateCount = "UPDATE events SET current_attendance = 1 WHERE event_id = %s"
#             cursor.execute(updateCount, (eventID,))
            
#         else:
#             raise Exception('Error: Room already booked for that time')
#     else:
#         raise Exception('ERROR: Room capacity exceeded')
#     cnx.commit()

#     return render_template(
#     'eventsubmitted.html',
#     name = name,
#     description = description,
#     expected_attendance = expected_attendance,
#     venue_id = venue_id,
#     event_owner = event_owner,
#     start_time = start_time)



