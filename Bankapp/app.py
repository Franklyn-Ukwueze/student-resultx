import json
import pymongo
from customer import Customer

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["bank_app"]
my_collection = db["customer_data"]

def add_new_cutomer(name=""):
    split_input = []
    if name:
        split_input.append(name)
        #split_input = [name]
    else:
        user_input = input("Enter CUSTOMER NAME, PHONE NUMBER, GENDER and DATE OF BIRTH.\nThen press enter.")

        split_input = user_input.split(', ')

        if len(split_input) < 4: return None

        for i in range(len(split_input)):
            split_input[i] = split_input[i].strip()

    existing_customer = customer_exists(split_input[0])
    if existing_customer:
        print(f"{split_input[0]} already exists as a customer.\nThank you.")
        existing_customer.pop("_id")
        customer_info = Customer(**existing_customer)
        # customer_info = Customer(
        #      name=existing_customer["name"],
        #      phone_number=existing_customer["phone_number"],
        #      gender=existing_customer["gender"],
        #      D_O_B=existing_customer["date_of_birth"],
        #      account_number=existing_customer["account_number"],
        #      transactions=existing_customer["transactions"],
        #      balance=existing_customer["balance"]
        #  )
        return customer_info
    else:
        new_customer = Customer(
            split_input[0],
            split_input[1],
            split_input[2],
            split_input[3]
        )

        #data = json.dumps(new_customer.print())
        #save_data(data[1:-1])
        save_data(new_customer.print())

    # Frank = Customer("Frank Ukwueze", "09087654321", "Male","19/03/2002")
    # Sam = Customer('Sam Nweke', "07097654321", "Male", "17/11/2000")

    print(f"New customer's full info is:\n {new_customer.print()}\n")
    # print(f"Only the account number: {new_customer.account_number}")
    return new_customer

def save_data(data):
    # with open("customer_data.txt", 'a') as customer_file:
    #     customer_file.write(data)
    #     customer_file.write('\n')

    my_collection.insert_one(data)
    

def customer_exists(customer_data):
    # data = None
    # with open("customer_data.txt") as customer_file:
    #     data = customer_file.read()
    data = my_collection.find_one({'name': customer_data})
    if data:
        print(data)
        return data
    else:
        return None

def transfer(sender_name, receiver_name, receiver_account_number, receiver_bank, amount):        
     customer = add_new_cutomer(sender_name)
     if customer:
         customer.balance = 1000000
         customer.send_money(receiver_name, receiver_account_number, receiver_bank, amount)
       
         update_filter = {"account_ number": customer.account_number}
         update_value = { "$set": {"transactions": customer.transactions} }
         my_collection.update_one(update_filter, update_value)

         data = my_collection.find_one({"account_number": customer.account_number})
         print(data)

sender, receiver, account, bank, amount = "Franklyn Ifechukwu", "Samson Onyebuchi", 3237654321, "Fidelity Bank", 30000
transfer(sender, receiver, account, bank, amount)
#result = add_new_cutomer("Franklyn Ifechukwu")
