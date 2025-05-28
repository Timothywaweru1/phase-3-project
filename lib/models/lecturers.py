class Lecturer:
    def __init__(self, lecturer_id, name, department):
        self.lecturer_id = lecturer_id
        self.name = name
        self.department = department

    def __repr__(self):
        return f"<Lecturer {self.lecturer_id}: {self.name}>"
