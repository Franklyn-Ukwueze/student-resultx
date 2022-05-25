from student import Student

name = input("\nEnter name for new student: ")
age = input("\nEnter age for new student: ")
gender = input("\nEnter student gender: ")

new_student = Student(name,age,gender,)
print (f"\nMy name is {new_student.name} and I am {new_student.age} years old. ")

new_student.enter_score()

scores_dict = new_student.subjects

header = f"""
===========================================
Welcome to TechApprentice Academy.
Final RESULT SHEET.
-------------------------------------------
Student Name: {new_student.name}
Student Age: {new_student.age}
Student Gender: {new_student.gender}
===========================================
"""
average_score = 0

for x in scores_dict.keys():
    y = scores_dict[x]
    print(f'{x}: {y[-1]}')
    average_score += y[-1]

current_average = average_score / len(scores_dict)

remarks = " "
if current_average <= 40:
    remarks = 'Poor'
elif current_average > 40 and current_average <= 50:
    remarks = 'Fair'
elif current_average > 50 and current_average <= 60:
    remarks = 'Pass'
elif current_average > 60 and current_average <= 75:
    remarks = 'Good'
elif current_average > 75 and current_average <= 90:
    remarks = 'Very Good'
else:
    remarks = 'Outstanding'

footer = f"""
===========================================
Average: {current_average}
Comment: {remarks}
===========================================
"""

with open('results.txt', 'x') as results:
    results.write("Your file is being created...")
    results.write(header)
    results.write("Subjects:")
    for x in scores_dict.keys():
        y = scores_dict[x] 
        results.write(f'\n{x}: {y[-1]}')
    results.write(footer)

"""
    ===========================================
    |Welcome to TechApprentice Academy.          
    |Final RESULT SHEET.
    |-------------------------------------------
    |Student Name: 
    |Student Age: 
    |Student Gender: 
    |===========================================
     
     
     Subjects: 
    ===========================================
    Average: 
    Comment:
    ===========================================
    """