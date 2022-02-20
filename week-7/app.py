from flask import Flask, request, redirect, render_template, session, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'session secret key' 


# mysql connection
db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="7777777", 
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

    sql = "INSERT INTO members (name, username, password) VALUES (%s, %s, %s)"
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
    sql = "SELECT * FROM members WHERE username = %s AND password = %s"
    val = (input_userName, input_Password)
    
    
    try:
        Cursor.execute(sql,val)

        result = Cursor.fetchall()
        input_name = result[0][0] 
        input_username = result[0][1]
        session['LogIn'] = input_name
        session['username'] = input_username

        return redirect(url_for('succeed', name=input_name))
        
    except:

        if input_userName=='' or input_Password=='':
            error_message = '請輸入帳號、密碼'
        else:
            error_message = '帳號或密碼輸入錯誤'
        return redirect(url_for('fail',message=error_message)) 

@app.route('/api/members')
def search():
    try:
        member_query_string = request.args.get('username')
        sql = "SELECT * FROM members WHERE username = %s"
        val = tuple(member_query_string)
        output_json = {"data":None}

        try:
            Cursor.execute(sql,val)
            result = Cursor.fetchall()
            search_id = result[0][3]
            search_name = result[0][0] 
            data = {'id':search_id, 'name':search_name, 'username':member_query_string}
            output_json['data'] = data
            return output_json

        except:
            return output_json

    except:
        ### show a collection of members ###
        sql = "SELECT * FROM members"
        current_members = {"data":[]}
        Cursor.execute(sql)
        results = Cursor.fetchall()
        member_info = {'id':0, 'name':0, 'username':0}
        for m in results:
            member_info['id'] = m[3]
            member_info['name'] = m[0]
            member_info['username'] = m[1]
            current_members['data'].append(member_info)

        return current_members

# 更新會員姓名
@app.route('/update_username',methods=['POST'])
def update_username():
    
    if 'LogIn' in session:
        update_json = {"ok":True}
        update_Name = request.get_json()['name']
        
        ### session change; update username with mysql ###
        original_username = session['username'] 
        
        sql = "UPDATE members SET name = %s WHERE username = %s"
        val = (update_Name,original_username)
        Cursor.execute(sql,val)
        db.commit()

        session['LogIn'] = update_Name

        return render_template('succeed.html', response=update_json)

    else:
        error_json = {'error':True}
        return render_template('succeed.html', response=error_json)




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
    session.pop('username', None)
    return redirect(url_for('index'))

app.run(port=3000, debug=True)
