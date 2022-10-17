def get_number(display_message=""):
    """
    This function prints a message and checks if user input can be converted to int,
    if it can it returns the int of the input else it continues to print the message
    until user enters the right input 
    """
    num = input(display_message)
    while not num.isnumeric():
        num = input(display_message)

    return int(num)

def display(message):
    """S
    This function returns a message
    """
    return message 