from flask import Flask, render_template, url_for, request, redirect, session, flash, g
from functools import wraps
import  md5, string, math, re, sqlite3

app = Flask(__name__)

# config
app.config.from_object('config.DevelopmentConfig')
app.logdata = "login.db"


def hashpass(password):
    m = md5.new()
    m.update(password)
    hashed = m.hexdigest()
    return hashed


def cleaninput(text):
    validtext = (string.ascii_letters + string.digits + "!@#$%^*()")
    text = filter(lambda x: x in validtext, text)
    return text


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    return render_template("index.html")


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        g.db = connect_db()
        Username = request.form['username']
        Pass = request.form['password']
        Pass2 = request.form['password2']
        c = g.db.execute("SELECT * FROM posts WHERE username ='%s'" % Username)
        if Username != cleaninput(Username) or Pass != cleaninput(Pass):
            error = "Invalid username or password"
        elif Pass != Pass2:
            error = "Please confirm that your passwords are the same"
        elif c.fetchone() is not None:
            error = "Username already chosen"
        else:
            g.db.execute('INSERT INTO posts VALUES (?,?)', (Username, hashpass(Pass)))
            g.db.commit()
            flash('Account Registered')
            g.db.close()
            return redirect(url_for('register'))
        g.db.close()
    return render_template("register.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['mode'] == "Register":
            return redirect(url_for('register'))
        elif request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))


def connect_db():
    return sqlite3.connect(app.logdata)

if __name__ == '__main__':
    app.run()
