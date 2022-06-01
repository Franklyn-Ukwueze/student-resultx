import json
from customer import Customer


# print('\n',Sam)



def add_new_cutomer():
    user_input = input("Enter CUSTOMER NAME, PHONE NUMBER, GENDER and DATE OF BIRTH.\nThen press enter.")

    split_input = user_input.split(', ')

    for i in range(len(split_input)):
        split_input[i] = split_input[i].strip()

    if customer_exists(split_input):
        print(f"{split_input[0]} already exists as a customer.\nThank you.")
    else:
        new_customer = Customer(
            split_input[0],
            split_input[1],
            split_input[2],
            split_input[3]
        )
        data = json.dumps(new_customer.print())
        save_data(data)
    # Frank = Customer("Frank Ukwueze", "09087654321", "Male","19/03/2002")
    # Sam = Customer('Sam Nweke', "07097654321", "Male", "17/11/2000")

    print(f"New customer's full info is:\n {new_customer.print()}\n")
    print(f"Only the account number: {new_customer.account_number}")

def save_data(data):
    with open("customer_data.txt", 'a') as customer_file:
        customer_file.write(data)
        customer_file.write('\n')

def customer_exists(customer_data):
    data = None
    with open("customer_data.txt") as customer_file:
        data = customer_file.read()
    if data:
        print(data)
        return True
    else:
        return False
        
add_new_cutomer()
