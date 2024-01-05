def number_of_students():
    return int(input("Enter the number of students: "))

def stu_info():
    students = {}
    n = number_of_students()
    for _ in range(n):
        student_id = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        students[student_id] = {'name': name, 'dob': dob}
    return students

def number_of_courses():
    return int(input("Enter the number of courses: "))

def course_info():
    courses = {}
    n = number_of_courses()
    for _ in range(n):
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        courses[course_id] = course_name
    return courses

def stu_marks(students, courses):
    marks = {course_id: {} for course_id in courses}
    for course_id in courses:
        print(f"\nEntering marks for {courses[course_id]}")
        for student_id in students:
            mark = float(input(f"Enter mark for {students[student_id]['name']} (ID: {student_id}): "))
            marks[course_id][student_id] = mark
    return marks

def print_summary_table(students, courses, marks):
    # Prepare the header
    header_line = "ID         Name                Date of Birth   " + "".join([f"{course_name[:10]:<12}" for course_name in courses.values()])
    print(header_line)
    print('-' * len(header_line))

    # Print student rows
    for student_id, student_info in students.items():
        # Prepare the student's basic info
        student_row = f"{student_id:<10}{student_info['name']:<20}{student_info['dob']:<18}"

        # For each course, add the mark to the row
        for course_id in courses:
            mark = marks[course_id].get(student_id, 'N/A')
            student_row += f"{mark:<12}"
        
        print(student_row)
    
    print('-' * len(header_line))

# Initialize data structures
students = stu_info()
courses = course_info()
marks = stu_marks(students, courses)

print_summary_table(students, courses, marks)
