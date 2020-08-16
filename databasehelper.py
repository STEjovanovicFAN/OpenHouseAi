import sqlite3

def initDB(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS user (
                        sessionId TEXT PRIMARY KEY,
                        id TEXT NOT NULL
                    ); """)

        cur.execute("""CREATE TABLE IF NOT EXISTS action (
                        time DATETIME DEFAULT CURRENT_TIMESTAMP,
                        user_sessionId TEXT,
                        type TEXT NOT NULL,
                        locationX INTEGER,
                        locationY INTEGER,
                        viewedId TEXT,
                        pageFrom TEXT,
                        pageTo TEXT,
                        FOREIGN KEY (user_sessionId) REFERENCES user(sessionId)
                    ); """)
        conn.commit()                  
        cur.close()
    except Error as e:
        print(e)


