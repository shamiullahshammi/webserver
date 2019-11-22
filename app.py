from flask import Flask, g, render_template
import sqlite3
import os
from datetime import date, datetime
DATABASE = "./one.db"

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE status (ID INTEGER PRIMARY KEY,gpio INTEGER,status TEXT);")
    conn.commit()
    conn.commit()


# helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# helper to closue
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    conn = sqlite3.connect(DATABASE)
    cur = get_db().cursor()
    fh = open("/sys/class/gpio/gpio10/value", "r")
    ch=fh.readlines()
    now = datetime.now()
    for j in (ch):
        c=j[0]
        if c == '0':
                cur.execute("INSERT INTO status (gpio,status) VALUES(10,'ON');")
                conn.commit()	
                res = cur.execute("select * from status")
                return render_template("index.html", status=res)
        elif c == '1':
                cur.execute("INSERT INTO status (gpio,status) VALUES(10,'OFF');")
                conn.commit()
                res = cur.execute("select * from status")
                return render_template("index.html", status=res)
		
    res = cur.execute("select * from status")
    conn.commit()
    return render_template("index.html", status=res)

if __name__ == '__main__':
    app.run(host="192.168.1.188",debug=True,port=8050)


