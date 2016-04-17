from flask import Flask, render_template, url_for, request, redirect, session, flash, g
from functools import wraps
import  md5, string, math, re, sqlite3, json

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
            a_dict = {Username: {"savedBooks": [], "likedBooks": [], "dislikedBooks": [], "tagRanks": {}}}
            with open('userdata.json') as f:
                data = json.load(f)
            data.update(a_dict)
            with open('userdata.json', 'w') as f:
                json.dump(data, f)
            return redirect(url_for('login'))
        g.db.close()
    return render_template("register.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        Username = request.form['username']
        Pass = request.form['password']
        g.db = connect_db()
        c1 = g.db.execute("SELECT pass FROM posts WHERE username ='%s'" %Username)
        c2 = g.db.execute("SELECT * FROM posts WHERE username ='%s'" %Username)
        passpull = c1.fetchone()
        if request.form['mode'] == "Register":
            return redirect(url_for('register'))
        elif passpull[0] != hashpass(Pass) or c2.fetchone()[0] != Username:
            error = passpull[0] + " : " + hashpass(Pass)
        else:
            session[Username] = True
            flash('You were logged in')
            return redirect('home', username=Username)
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    Username = request.form['username']
    session.pop(Username, None)
    return redirect(url_for('welcome'))


def connect_db():
    return sqlite3.connect(app.logdata)

if __name__ == '__main__':
    app.run()
