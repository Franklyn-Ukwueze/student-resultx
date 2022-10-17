from studentdb import *





print("Welcome to Student...")
instr = input("To register student enter R\nTo find student enter F\nTo update student score enter U\nTo quit enter Q\n ").lower()
while instr != "q":
    if instr == 'r':
        add_new_student()

    if instr == 'f':
        find_student()

    if instr == 'u':
        update_score()

    instr = input("To register student enter R\nTo find student enter F\nTo update student score enter U\nTo quit enter Q\n ").lower()

print("Program terminated!\nGood bye.")