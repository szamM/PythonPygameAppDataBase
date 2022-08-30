import sqlite3 as sql

db = sql.connect('us_data.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)""")


def checker(user_data):
    logins = cur.execute("SELECT * FROM users").fetchall()
    login, password = user_data[0], user_data[1]
    user__data = (str(login), str(password))
    if user__data in logins:
        return False
    else:
        cur.execute("INSERT INTO users VALUES(?, ?);", user_data)
        db.commit()
        return True
