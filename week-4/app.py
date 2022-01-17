from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = 'session secret key' 

error_message = ''

@app.route('/')
def index():
    if 'LogIn' in session:
        return render_template('succeed.html')
    else:
        return render_template('homePage.html')

@app.route('/signin', methods=['POST'])
def login():
    input_userName = request.form['username']
    input_password = request.form['password']
    if input_userName=='test' and input_password=='test':
        return redirect(url_for('succeed'))
    else:
        global error_message
        if input_userName=='' or input_password=='':
            error_message = '請輸入帳號、密碼'
        else:
            error_message = '帳號、或密碼輸入錯誤'
        return redirect('/error')


@app.route('/menber')
def succeed():
    session['LogIn'] = True
    return render_template('succeed.html')

@app.route('/error',methods=['GET','POST'])
def fail():
    if error_message=='':
        error_query_string = request.args['message']
        return render_template('fail.html',message=error_query_string)
    return render_template('fail.html',message=error_message)

@app.route('/signout')
def logOut():
    session.pop('LogIn', None)
    return redirect(url_for('index'))

app.run(port=3000, debug=True)
