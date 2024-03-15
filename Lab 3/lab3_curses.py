import curses
import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class ECT:
    def __init__(self, ects):
        self.ects = ects

class StudentMarkManagement:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.ects = {}

    def add_student(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Adding Student")
        self.stdscr.refresh()

        student_id = self.get_input("Student ID: ")
        name = self.get_input("Full Name: ")
        dob = self.get_input("Date of Birth (dd/mm/yyyy): ")
        self.students[student_id] = Student(student_id, name, dob)

    def add_course(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Adding Course")
        self.stdscr.refresh()

        course_id = self.get_input("Course ID: ")
        course_name = self.get_input("Course Name: ")
        self.courses[course_id] = Course(course_id, course_name)

    def enter_ect(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Entering ECTs")
        self.stdscr.refresh()

        for course_id, course in self.courses.items():
            ect = int(self.get_input(f"Enter ECTs for {course.course_name}: "))
            self.ects[course_id] = ECT(ect)            

    def enter_mark(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Entering Marks")
        self.stdscr.refresh()

        for course_id, course in self.courses.items():
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"Entering marks for {course.course_name}")
            self.stdscr.refresh()

            self.marks[course_id] = {}
            for student_id, student in self.students.items():
                mark = self.get_float_input(f"Enter mark for {student.name} (ID: {student_id}) (Decimal number please, example: 19.00): ")
                self.marks[course_id][student_id] = mark

    def calculate_gpa(self, student_id):
        gpa_list = []
        sum_ects = sum(self.ects[course_id].ects for course_id in self.ects)
        
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
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Summary Table")
        
        header_line = "ID         Name                Date of Birth   "
        for course_id, course in self.courses.items():
            header_line += f"{course.course_name[:10]} (ECTs: {self.ects[course_id].ects}) "
        self.stdscr.addstr(2, 0, header_line)
        self.stdscr.addstr(3, 0, '-' * len(header_line))

        line_number = 4
        for student_id, student in self.students.items():
            student_row = f"{student.student_id:<10}{student.name:<20}{student.dob:<18}"
            for course_id in self.courses:
                mark = self.marks.get(course_id, {}).get(student_id, 'N/A')
                student_row += f"{mark:<18}"
            self.stdscr.addstr(line_number, 0, student_row)
            line_number += 1
        
        self.stdscr.addstr(line_number, 0, '-' * len(header_line))
        self.stdscr.refresh()
        self.stdscr.getch()

    def get_input(self, prompt):
        curses.echo()
        self.stdscr.addstr(2, 0, prompt)
        self.stdscr.refresh()
        try:
            user_input = self.stdscr.getstr(3, len(prompt), 20).decode('utf-8')
        except curses.error:
            user_input = ""
        curses.noecho()
        return user_input

    def get_float_input(self, prompt):
        curses.echo()
        self.stdscr.addstr(2, 0, prompt)
        self.stdscr.refresh()
        try:
            user_input = float(self.stdscr.getstr(3, len(prompt), 20).decode('utf-8'))
        except (curses.error, ValueError):
            user_input = 0.0
        curses.noecho()
        return user_input

def main(stdscr):
    system = StudentMarkManagement(stdscr)

    num_students = int(system.get_input("Enter the number of students: "))
    for _ in range(num_students):
        system.add_student()

    num_courses = int(system.get_input("Enter the number of courses: "))
    for _ in range(num_courses):
        system.add_course()

    system.enter_mark()
    system.enter_ect()
    system.summary_table()
    
    sorted_students = system.sort_students_by_gpa()
    system.stdscr.clear()
    system.stdscr.addstr(0, 0, "Sorted Students by GPA:")
    line_number = 2
    for student in sorted_students:
        system.stdscr.addstr(line_number, 0, f"ID: {student.student_id}, Name: {student.name}, GPA: {system.calculate_gpa(student.student_id)}")
        line_number += 1
    system.stdscr.refresh()
    system.stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
 # :) chiu roi 