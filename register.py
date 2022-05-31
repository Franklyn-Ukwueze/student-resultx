from student import Student

number_of_students = int(input('\nHow many students are you registering? '))
for x in range (number_of_students):
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

    with open('results.txt', 'a') as results:
        results.write(header)
        results.write("Subjects:")
        for x in scores_dict.keys():
            y = scores_dict[x] 
            results.write(f'\n{x}: {y[-1]}')
        results.write(footer)

    resultsgrouped = f"""
    Student: {new_student.name}
    Average: {current_average}
    Comment: {remarks}
    _______________________________________
    """    
    class_average = 0
    class_average += current_average
    new_classaverage = class_average / number_of_students 

    with open('classresult.txt', 'a') as classresult:
        for x in range(number_of_students):
            classresult.write(resultsgrouped)
        classresult.write(f"Class Average: {new_classaverage}")



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