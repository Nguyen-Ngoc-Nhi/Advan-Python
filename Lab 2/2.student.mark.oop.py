class student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class student_mark_management:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def add_student(self):
        student_id = input("Student ID: ")
        name = input("Full Name: ")
        dob = input("Date of Birth (dd/mm/yyyy): ")
        self.students[student_id] = student(student_id, name, dob)

    def add_course(self):
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        self.courses[course_id] = course(course_id, course_name)

    def enter_mark(self):
        for course_id, course in self.courses.items():
            print(f"\nEntering marks for {course.course_name}")
            self.marks[course_id] = {}
            for student_id, student in self.students.items():
                mark = float(input(f"Enter mark for {student.name} (ID: {student_id}): "))
                self.marks[course_id][student_id] = mark

    def summary_table(self):
        header_line = "ID         Name                Date of Birth   " + "".join([f"{course.course_name[:10]:<12}" for course in self.courses.values()])
        print(header_line)
        print('-' * len(header_line))

        for student_id, student in self.students.items():
            student_row = f"{student.student_id:<10}{student.name:<20}{student.dob:<18}"
            for course_id in self.courses:
                mark = self.marks.get(course_id, {}).get(student_id, 'N/A')
                student_row += f"{mark:<12}"
            print(student_row)
        
        print('-' * len(header_line))

def main():
    system = student_mark_management()

    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        system.add_student()

    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        system.add_course()

    system.enter_mark()
    system.summary_table()

if __name__ == "__main__":
    main()
    
"""
lab 1: 
    structured by functions
    data is passed around functions and manipulated directly
    program execute one after another.
    data store in dictionary
lab 2: 
    using oop principles
    structured around objects, encapsulate both data and methods that operate on that data
    data use encapsulate within object 
    
"""