greeting = input("Greeting: ").strip()
greeting = greeting.lower()

if greeting[:5] == "hello":
    print("$0")
elif greeting[:5] != "hello" and greeting[0] == "h":
    print("$20")
else:
    print("$100")
