def main():
    s = input("Type in a sentence. ")
    s= convert(s)
    print(s)

def convert(sentence):
    emoji = {":)": "🙂",":(": "🙁"}
    output = ""
    user_input = sentence.split()
    for word in user_input:
        output += emoji.get(word, word) + " "
    return output.strip()

main()