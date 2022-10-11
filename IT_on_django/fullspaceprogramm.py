import sqlite3



with sqlite3.connect('db.sqlite3') as db:
    sqlCursor = db.cursor()
    sqlCursor.execute()