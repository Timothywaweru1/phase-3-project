class Course:
    def __init__(self, course_id, name, lecturer_id):
        self.course_id = course_id
        self.name = name
        self.lecturer_id = lecturer_id
        self.students = []  

    def add_student(self, student):
        self.students.append(student)

    def __repr__(self):
        return f"<Course {self.course_id}: {self.name}>"
