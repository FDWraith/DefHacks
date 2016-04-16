import sqlite3

with sqlite3.connect("login.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE posts(username text, pass text)""")
