from student import Student

name = input("\nEnter name for new student: ")
age = input("\nEnter age for new student: ")
gender = input("\nEnter student gender: ")

new_student = Student(name,age,gender)
print (f"\nMy name is {new_student.name} and I am {new_student.age} years old. ")

new_student.enter_score()

print(f"\nSubjects for {new_student.name} are:\n{new_student.subjects}")

