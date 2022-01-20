# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = 'session secret key' 

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

        if input_userName=='' or input_password=='':
            error_message = '請輸入帳號、密碼'

        else:
            error_message = '帳號、或密碼輸入錯誤'

        return redirect(url_for('fail',message=error_message))


@app.route('/member/')
def succeed():
    if 'LogIn' in session:
        return render_template('succeed.html')
    else:
        return redirect(url_for('index'))


#@app.route("/error/<message>")
@app.route('/error/')
#def fail(message):
def fail():
    #return render_template('fail.html',message=message)
    #error_query_string = request.args['message']
    error_query_string = request.args.get('message')
    return render_template('fail.html',message=error_query_string)


@app.route('/signout')
def logOut():
    session.pop('LogIn', None)
    return redirect(url_for('index'))

app.run(port=3000, debug=True)
