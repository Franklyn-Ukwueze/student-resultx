from random import randint

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n > 0:
        break
level = randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess < level:
            print("Too small!", end="\n")
            continue
        elif guess > level:
            print("Too large!", end="\n")
            continue
        else:
            print("Just right!", end="\n")
            break