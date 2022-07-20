class Student:
    def __init__(self, name, age, gender, students_class, subjects=[], scores = {}, total_score = 0):
        """
        Create students with the following details; name, age, gender, class, subjects offered,
        scores in those subjects and total score.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.students_class = students_class
        self.subjects = subjects 
        self.scores = scores
        self.total_score = total_score

    def print(self):
        return self.__dict__
