class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.courses = [] 

    def enroll(self, course):
        self.courses.append(course)

    def __repr__(self):
        return f"<Student {self.student_id}: {self.name}>"
