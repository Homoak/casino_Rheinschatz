import sqlite3

def init():
    connection = sqlite3.connect('database.db')
    sqllite_create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    password TEXT NOT NULL,
                                    email TEXT NOT NULL UNIQUE);'''
    cursor = connection.cursor()
    cursor.execute(sqllite_create_table_query)
    connection.commit()
    connection.close()

init()