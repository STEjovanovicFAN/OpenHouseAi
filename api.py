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

#default page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Open House AI Demo </h1>
<p>Api demo for the purposes of the coding challenge from Open House Ai</p>'''

@app.errorhandler(400)
def bad_request(e):
    return "<h1>400</h1><p>Bad request. Make sure your params are correct.</p>", 400

#get all users and sessions, for testing 
@app.route('/api/v1/resources/user/all', methods=['GET'])
def api_users_all():
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    res = cur.execute('SELECT * FROM user;').fetchall()
    conn.commit()
    cur.close()
    return jsonify(res)

#insert user and session, for front end
@app.route('/api/v1/resources/user', methods=['POST'])
def api_user():
    query_parameters = request.args
    
    id = query_parameters.get('id')
    sessionId = query_parameters.get('sessionId')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        sqlite_insert_with_param  = """ INSERT INTO user 
                    (id, sessionId)
                    VALUES 
                    (?, ?)"""
        data_tuple = (id, sessionId)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        cur.close()
    except Error as e:
        return bad_request(400)
        print(e)

    return(jsonify("200"))    

#get all actions, for testing
@app.route('/api/v1/resources/action/all', methods=['GET'])
def api_actions_all():
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    res = cur.execute('SELECT * FROM action;').fetchall()
    conn.commit()
    cur.close()
    return jsonify(res)

#insert action, for front end
@app.route('/api/v1/resources/action', methods=['POST'])
def api_action():
    query_parameters = request.args
    
    user_sessionId = query_parameters.get('user_sessionId')
    type_text = query_parameters.get('type')
    locationX = query_parameters.get('locationX')
    locationY = query_parameters.get('locationY')
    viewedId = query_parameters.get('viewedId')
    pageFrom = query_parameters.get('pageFrom')
    pageTo = query_parameters.get('pageTo')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        sqlite_insert_with_param  = """ INSERT INTO action 
                    (user_sessionId, type, locationX, locationY, viewedId, pageFrom, pageTo)
                    VALUES 
                    (?, ?, ?, ?, ?, ?, ?)"""
        data_tuple = (user_sessionId, type_text, locationX, locationY, viewedId, pageFrom, pageTo)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        cur.close()
    except Error as e:
        return bad_request(400)
        print(e)

    return(jsonify("200"))    

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
        cur.close()
    except Error as e:
        print(e)

initDB()
app.run()