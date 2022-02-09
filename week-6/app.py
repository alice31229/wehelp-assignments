# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

from flask import Flask, request, redirect, render_template, session, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'session secret key' 


# mysql connection
db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="666666", 
    database="accounts"
    )
Cursor = db.cursor()


@app.route('/')
def index():
    if 'LogIn' in session:
        return redirect(url_for('succeed'))
    else:
        return render_template('homePage.html')

@app.route('/signup', methods=['POST'])
def signUp():
    input_name = request.form['name'] 
    input_userName = request.form['username']
    input_password = request.form['password']

    if input_name.strip()=='' and input_userName.strip()=='' and input_password.strip()=='':
        error_message = '請輸入姓名、帳號、密碼'
        return redirect(url_for('fail',message=error_message))

    sql = "INSERT INTO members VALUES (%s, %s, %s)"
    val = (input_name, input_userName, input_password)


    try: # success
        Cursor.execute(sql, val)
        db.commit()

        return redirect(url_for('index'))

    except: # fail
        error_message = '帳號已經被註冊'
        return redirect(url_for('fail',message=error_message))
        


@app.route('/signin', methods=['POST'])
def login():

    input_userName = request.form['userName']
    input_Password = request.form['Password']
    sql = f"SELECT * FROM members WHERE username = '{input_userName}' AND password = '{input_Password}'"
    
    
    try:
        Cursor.execute(sql)

        result = Cursor.fetchall()
        input_name = result[0][0] 
        session['LogIn'] = input_name

        return redirect(url_for('succeed', name=input_name))
        
    except:

        if input_userName=='' or input_Password=='':
            error_message = '請輸入帳號、密碼'
        else:
            error_message = '帳號或密碼輸入錯誤'
        return redirect(url_for('fail',message=error_message)) 



@app.route('/member/')
def succeed():
    if 'LogIn' in session:
        name = session['LogIn']
        return render_template('succeed.html',name=name)
    else:
        return redirect(url_for('index'))



@app.route('/error/')
def fail():
    error_query_string = request.args.get('message')
    return render_template('fail.html',message=error_query_string)


@app.route('/signout')
def logOut():
    session.pop('LogIn', None)
    return redirect(url_for('index'))

app.run(port=3000, debug=True)
