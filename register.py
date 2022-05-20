from student import Student

name = input("\nEnter name for new student: ")
age = input("\nEnter age for new student: ")
gender = input("\nEnter student gender: ")

new_student = Student(name,age,gender)
print (f"\nMy name is {new_student.name} and I am {new_student.age} years old. ")

new_student.enter_score()

print(
    f"""
    ===========================================
    Welcome to TechApprentice Academy.
    Final RESULT SHEET.
    -------------------------------------------
    Student Name: {new_student.name}
    Student Age: {new_student.age}
    Student Gender: {new_student.gender}
    ===========================================
    Subjects:
    ===========================================
    Average 
    Comment
    ===========================================
    """)