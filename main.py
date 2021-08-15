from flask import Flask, render_template, request, redirect, session
import mysql.connector
import re
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host="localhost", user="root", password="", database="registrationpydb")
cursor = conn.cursor()



@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
        users = cursor.fetchone()
        if users:
            session['loggedin']=True
            session['user_id']=users[0]
            session['email']=users[2]
            return redirect('/home')
        else:
            msg='Incorrect Username/Password'
            return render_template('login.html', msg=msg)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute(
            """SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
        users = cursor.fetchone()
        if users:
            session['loggedin'] = True
            session['user_id'] = users[0]
            session['email'] = users[2]
            return redirect('/home')
        else:
            msg = 'Incorrect Username/Password'
            return render_template('login.html', msg=msg)


@app.route('/add_feedback', methods=['POST'])
def add_feedback():
    fdexp=request.form.get('exp')
    fdname=request.form.get('fdname')
    fdemail=request.form.get('fdemail')
    fdage=request.form.get('fdage')
    fdphone=request.form.get('fdphone')
    fdmessage=request.form.get('fdmessage')

    cursor.execute("""INSERT INTO `feedback` (`id`,`exp`,`fdname`,`fdemail`,`fdage`,`fdphone`,`fdmessage`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')  """ .format(fdexp,fdname,fdemail,fdage,fdphone,fdmessage))
    conn.commit()
    return redirect('/feedback')


#@app.route('/logout')
#def logout():
    try:
        if session.pop('user_id'):
            return redirect('/')
    except KeyError:
        return redirect('/')

@app.route('/femaths-1plan')
def femathsplan():
    return render_template('femaths-1plan.html')

@app.route('/femaths-1imp')
def femathsimp():
    return render_template('femaths-1imp.html')

@app.route('/femaths-1vids')
def femathsvids():
    return render_template('femaths-1vids.html')

@app.route('/febooks')
def febooks():
    return render_template('febooks.html')

@app.route('/femaths-1')
def femaths():
    return render_template('femaths-1.html')

@app.route('/navigation')
def navigation():
    return render_template('navigation.html')

@app.route('/febee')
def bee():
    return render_template('febee.html')

@app.route('/febeeimp')
def beeimp():
    return render_template('febeeimp.html')

@app.route('/febeepapers')
def beepapers():
    return render_template('febeepapers.html')

@app.route('/febeeplan')
def beeplan():
    return render_template('febeeplan.html')

@app.route('/febeevids')
def beevids():
    return render_template('febeevids.html')

@app.route('/femaths-1book')
def mathsbook():
    return render_template('femaths-1book.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')



if __name__ == "__main__":
    app.run(debug=True)
