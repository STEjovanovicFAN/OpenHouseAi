import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
db_path = 'database/sqlite.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Open House AI Demo </h1>
<p>Api demo for the purposes of the coding challenge from Open House Ai</p>'''


def initDB():
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS user (
                        sessionId TEXT PRIMARY KEY,
                        id TEXT NOT NULL
                    ); """)

        cur.execute("""CREATE TABLE IF NOT EXISTS action (
                        time DATETIME DEFAULT CURRENT_TIMESTAMP,
                        user_sessionId TEXT,
                        type TEXT,
                        locationX INTEGER,
                        locationY INTEGER,
                        viewedId TEXT,
                        pageFrom TEXT,
                        pageTo TEXT,
                        FOREIGN KEY (user_sessionId) REFERENCES user(sessionId)
                    ); """)      

    except Error as e:
        print(e)

initDB()
app.run()