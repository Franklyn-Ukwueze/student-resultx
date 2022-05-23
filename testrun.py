#run_file  = open("textfile.txt","rt")
#print(type(run_file))
#text_complete = run_file.read()
#text_line = run_file.readline()
#print("\ntext_line: ", text_line)
#print("second line:\n", run_file.readline())
#run_file.close()

with open("textfile.txt") as run_file:
    text_complete = run_file.read()
    print("File still open...\n", text_complete)

additional_text = f"""
This is content from textfile.txt: \n{text_complete}
"""

with open('newtextfile.txt', 'a') as newtextfile:
    newtextfile.write("A new file is being created...")
    newtextfile.write(additional_text)
    