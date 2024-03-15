import math
import numpy as np

class student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class ECT:
    def __init__(self, ects):
        self.ects = ects

class student_mark_management:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.ects = {}

    def add_student(self):
        student_id = input("Student ID: ")
        name = input("Full Name: ")
        dob = input("Date of Birth (dd/mm/yyyy): ")
        self.students[student_id] = student(student_id, name, dob)

    def add_course(self):
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        self.courses[course_id] = course(course_id, course_name)
        
    def enter_ect(self):
        for course_id, course in self.courses.items():
            print(f"\nEntering ECTs")
            ect = int(input(f"Enter ECTs for {course.course_name}: "))
            self.ects[course_id] = ECT(ect)            

    def enter_mark(self):
        for course_id, course in self.courses.items():
            print(f"\nEntering marks for {course.course_name}")
            self.marks[course_id] = {}
            for student_id, student in self.students.items():
                mark = float(input(f"Enter mark for {student.name} (ID: {student_id}) (Decimal number please, example: 19.00): "))
                self.marks[course_id][student_id] = mark

    def calculate_gpa(self, student_id):
        gpa_list = []
        sum_ects = sum(self.ects[course_id].ects for course_id in self.ects)
        print("Total ECTs: ", sum_ects)
        
        for course_id, course_marks in self.marks.items():
            if student_id in course_marks:
                mark = course_marks[student_id]
                ect = self.ects[course_id].ects
                gpa_list.append((mark * ect) / sum_ects)
        return np.round(np.sum(gpa_list), 2)

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students.values(), key=lambda x: self.calculate_gpa(x.student_id), reverse=True)
        return sorted_students

    def summary_table(self):
        header_line = "ID         Name                Date of Birth   "
        for course_id, course in self.courses.items():
            header_line += f"{course.course_name[:10]} (ECTs: {self.ects[course_id].ects}) "
        print(header_line)
        print('-' * len(header_line))

        for student_id, student in self.students.items():
            student_row = f"{student.student_id:<10}{student.name:<20}{student.dob:<18}"
            for course_id in self.courses:
                mark = math.floor((self.marks.get(course_id, {}).get(student_id, 'N/A')) *10) / 10
                student_row += f"{mark:<18}"
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
    system.enter_ect()
    system.summary_table()
    
    sorted_students = system.sort_students_by_gpa()
    print("\nSorted Students by GPA:")
    for student in sorted_students:
        print(f"ID: {student.student_id}, Name: {student.name}, GPA: {system.calculate_gpa(student.student_id)}")

if __name__ == "__main__":
    main()