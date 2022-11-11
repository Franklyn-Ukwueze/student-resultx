def main():
    user_input = input("Greeting: ").strip()
    print(value(user_input))

def value(greeting):
    greeting = greeting.lower()
    if greeting[:5] == "hello":
        return "$0"
    elif greeting[:5] != "hello" and greeting[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__== "__main__":
    main()
    