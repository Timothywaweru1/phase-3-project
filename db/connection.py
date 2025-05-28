import sqlite3

def get_connection(db_name="university.db"):
    return sqlite3.connect(db_name)
