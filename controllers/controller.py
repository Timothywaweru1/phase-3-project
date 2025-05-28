from db.connection import get_connection

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses

def get_all_lecturers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers")
    lecturers = cursor.fetchall()
    conn.close()
    return lecturers
