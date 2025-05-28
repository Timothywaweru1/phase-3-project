from controllers.controller import controller

def main():
    print("Students enrolled in courses:")

    student_id = 1  
    courses = controller.get_courses_for_student(student_id)
    for course in courses:
        print(f"Student {student_id} enrolled in Course: {course}")

if __name__ == "__main__":
    main()
