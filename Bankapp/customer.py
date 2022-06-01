import random 


class Customer:
    def __init__(self, name, phone_number, gender, D_O_B):
        """
        create customer, ensure to add name, phone number, gender and date of birth.
        System will generate acccount number
        """
        self.name = name
        self.phone = phone_number
        self.gender = gender
        self.date_of_birth = D_O_B
        self.account_number = random.randint(1000000000, 9999999999) #generate random 10 digit number as account number
        self.balance = 0

    def send_money(self):
        pass

    def buy_airtime(self):
        pass

    def make_payments(self):
        pass

    def deposit_cash(self):
        pass

    def print(self):
        return self.__dict__