def slow_down():
    s = input("Type in a sentence. ")
    for i in s:
        if i == " ":
            s = s.replace(" ","...")
            
    print(s)
    
slow_down()