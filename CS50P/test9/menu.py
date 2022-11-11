import sys
from math_solver import *


print("Welcome to the  mathsolver program.")
instr = input("To solve a quadratic equation enter Q\nTo find simple interest enter S\nTo find the the length of one side of a right angle triangle enter T\nTo end the program enter E\n").lower()
while instr != "e":
    if instr == 'q':
        values = input("Enter the numeric values of the quadratic equation seperated by a comma and space(, )") 
        values = values.split(", ")
        if to_number(values) == "invalid character":
            sys.exit(to_number(values))
        else:
            param = to_number(values)
            print(quadratic(param[0], param[1], param[2]))
            

    elif instr == 's':
        values = input("Enter principal amount, interest rate and time period in numbers seperated by comma and space(, )")
        values = values.split(", ")
        if to_number(values) == "invalid character":
            sys.exit(to_number(values))
        else:
            a, b, c = to_number(values)[0], to_number(values)(1), to_number(values)(2)
            print(simple_intrest(a, b, c))

    elif instr == 't':
        values = input("Enter the lengths of the known sides and 0 for the unknown side in numbers seperated by comma and space(, )")
        values = values.split(", ")
        if to_number(values) == "invalid character":
            sys.exit(to_number(values))
        else:
            a, b, c = to_number(values)[0], to_number(values)(1), to_number(values)(2)
            print(pythagoras(a, b, c))

    instr = input("To solve a quadratic equation enter Q\nTo find simple interest enter S\nTo find the the length of one side of a right angle triangle enter T\nTo end the program enter E\n").lower()

print("Program terminated!\nGood bye.")