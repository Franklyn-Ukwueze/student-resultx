from helpers import *
import pymongo
from studentapp_model import Student

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Student_db"]
my_collection = db["student_data"]

def add_new_student(name=""):
    """
    This function registers a new student and saves student's details to database
    """
    split_input = []
    if name:
        split_input.append(name)
    else:
        user_input = input("Enter STUDENT NAME, AGE, GENDER, and CLASS.\nThen press ENTER\n")

        split_input = user_input.split(", ")

        if len(split_input) < 4 or len(split_input)> 4: 
            return None

        for i in range(len(split_input)):
            split_input[i] = split_input[i].strip()

        subject_input = input("Enter student's 3 subjects seperated by ','.")
        subjects = subject_input.split(", ")

        subject_scores = {}
        for i in subjects:
            score = get_number(f"Enter score for {i}:")

            subject_scores[i] = score
            

        
        score_list = []
        for score in subject_scores.values():
            score_list.append(score)

        total_score = sum(score_list)
    existing_student = student_exists(split_input[0])
    
    if existing_student:
        display(f"{split_input[0]} is already present in the database.\nThank you.")
        existing_student.pop("_id")

        student_info = Student(**existing_student)
        return student_info

    else:
        new_student = Student(
            split_input[0],
            split_input[1],
            split_input[2],
            split_input[3],
            subject_scores,
            total_score
        )

        save_data(new_student.print())
    display(f"New student's details are\n{new_student.print()}")

    return new_student

def save_data(data):
    """
    Saves student data to database
    """
    my_collection.insert_one(data)

def student_exists(student_data):
    """
    Checks for student in database, returns student data if student exists else it returns none
    """
    data = my_collection.find_one({"name": student_data})
    if data:
        return data
    else:
        return None

def find_student():
    """
    Searches database for student, if found it prints the student's 
    details else it prints 'Record not found.'
    """

    student_name = input("What is the name of the student you're looking for?\n")
    data = student_exists(student_name)

    if data:
        return data
    else:
        return "Record not found."

def update_score():
    """
    Updates score of student provided and new details to screen.
    """
    student_name = input("Enter name of student who's score you would like to update.\n")
    data = my_collection.find_one({"name": student_name}, { "_id": 0,"age": 0, "gender": 0,
                                "students_class": 0,"subjects":0})
    
    display(f"{student_name}'s scores are:\n{data}")

    number_of_subjects =int(input("Enter number of subjects student has registered. "))

    new_scores = {}
    for _ in range(number_of_subjects):
        data = input("Enter name of subject and new score seperated by ':'\n")

        temp = data.split(":")
        new_scores[temp[0]] = int(temp[1])

    score_list = []
    for score in new_scores.values():
        score_list.append(score)
    new_total = sum(score_list)

    update_filter = {"name":student_name}
    update_value = {"$set": {"scores": new_scores}}
    my_collection.update_one(update_filter, update_value)

    update_value = {"$set": {"total_score": new_total}}
    my_collection.update_one(update_filter, update_value)

    data = my_collection.find_one({"name": student_name})
    display(f"{student_name}'s new scores are:\n{data}")
    







