def main():
    user_input = input("Input: ")
    print(del_vowels(user_input))


def del_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = ""
    for character in word:
        if character.lower() not in vowels:
            no_vowels += character
    return no_vowels


if __name__ == "__main__":
    main()