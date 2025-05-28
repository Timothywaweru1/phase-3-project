from db.connection import get_connection


def enroll_student(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO enrollments (student_id, course_id) VALUES (?, ?)
    """, (student_id, course_id))
    conn.commit()
    conn.close()


def get_courses_for_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.course_id, c.name, c.lecturer_id
        FROM courses c
        JOIN enrollments e ON c.course_id = e.course_id
        WHERE e.student_id = ?
    """, (student_id,))
    results = cursor.fetchall()
    conn.close()
    return results
