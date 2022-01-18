from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = 'session secret key' 

error_message = ''

@app.route('/')
def index():
    if 'LogIn' in session:
        return redirect(url_for('succeed'))
    else:
        return render_template('homePage.html')

@app.route('/signin', methods=['POST'])
def login():
    input_userName = request.form['username']
    input_password = request.form['password']
    if input_userName=='test' and input_password=='test':
        session['LogIn'] = True
        return redirect(url_for('succeed'))
    else:
        session['username'] = input_userName
        session['password'] = input_password
        return redirect(url_for('fail'))


@app.route('/member')
def succeed():
    if 'LogIn' in session:
        return render_template('succeed.html')
    else:
        return redirect(url_for('index'))

@app.route('/error')
def fail():
    try:
        error_query_string = request.args['message']
        return render_template('fail.html',message=error_query_string)
    except:
        userName = session['username']
        password = session['password']
        if userName=='' or password=='':
            error_message = '請輸入帳號、密碼'
        else:
            error_message = '帳號、或密碼輸入錯誤'
        return render_template('fail.html',message=error_message)

@app.route('/signout')
def logOut():
    session.pop('LogIn', None)
    return redirect(url_for('index'))

app.run(port=3000, debug=True)
