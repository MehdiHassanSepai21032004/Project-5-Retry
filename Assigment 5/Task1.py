student_marks = {"Alice": 85, "charlie": 55, "mark": 56}

name = input("Enter the studen's name: ")

marks = student_marks.get(name, "Student not found.")
if marks != "Student not found":
    print(f"{name}'s marks: {marks}")
else:
    print(marks)