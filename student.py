class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {}

    def enter_score(self):
        number_of_subjects = int(input(f'\nHow many subjects would you like to register for {self.name}? '))

        for x in range(number_of_subjects):
            subject_name = input(f'\nEnter name of subject - {x+1}: ')
            number_of_scores = 3
            score_list = []

            for y in range(1, number_of_scores + 1):
                score = int(input(f'Enter score for {subject_name}: '))
                score_list.append(score)

            total = sum(score_list)
            score_list.append(total)
            self.subjects[subject_name] = score_list
