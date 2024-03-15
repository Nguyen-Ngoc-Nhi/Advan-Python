import os
import zlib  # Import zlib for compression

from input import *
from output import *
from domains.student import Student
from domains.course import Course
from domains.ect import ECT

import math
import numpy as np

class StudentMarkManagement:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.ects = {}

    def add_student(self):
        student_id = input("Student ID: ")
        name = input("Full Name: ")
        dob = input("Date of Birth (dd/mm/yyyy): ")
        self.students[student_id] = Student(student_id, name, dob)

    def add_course(self):
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        self.courses[course_id] = Course(course_id, course_name)
        
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
        
    def write_to_file(self, file_name, data):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, file_name)
        with open(file_name, 'w') as file:
            for item in data:
                file.write(f"{item}\n")

    def compress_data(self, file_name, data):
        compressed_data = zlib.compress("\n".join(data).encode())
        with open(file_name, 'wb') as file:
            file.write(compressed_data)

    def decompress_data(self, file_name):
        with open(file_name, 'rb') as file:
            decompressed_data = zlib.decompress(file.read()).decode().split("\n")
        return decompressed_data

def main():
    system = StudentMarkManagement()

    # Check if students.dat exists, if yes, decompress and load data
    if os.path.exists("students.dat"):
        decompressed_data = system.decompress_data("students.dat")
        # Load data from decompressed file
        # Implement logic to load data into system.students, system.courses, etc.
    else:
        num_students = int(get_input("Enter the number of students: "))
        for _ in range(num_students):
            system.add_student()

        num_courses = int(get_input("Enter the number of courses: "))
        for _ in range(num_courses):
            system.add_course()

        system.enter_mark()
        system.enter_ect()
        system.summary_table()
    
        sorted_students = system.sort_students_by_gpa()
        display_message("\nSorted Students by GPA:")
        for student in sorted_students:
            display_message(f"ID: {student.student_id}, Name: {student.name}, GPA: {system.calculate_gpa(student.student_id)}")

        # Writing data to files
        system.write_to_file("students.txt", [str(student) for student in system.students.values()])
        system.write_to_file("courses.txt", [str(course) for course in system.courses.values()])
        system.write_to_file("marks.txt", [str(mark) for mark in system.marks.items()])

        # Compress data before closing the program
        system.compress_data("students.dat", [str(student) for student in system.students.values()])

if __name__ == "__main__":
    main()
