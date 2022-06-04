import random 
from transactions import Transactions

class Customer:
    def __init__(self, name, phone_number, gender, D_O_B, account_number=0, transactions={}, balance=0):
        """
        create customer, ensure to add name, phone number, gender and date of birth.
        System will generate acccount number
        """
        self.name = name
        self.phone = phone_number
        self.gender = gender
        self.date_of_birth = D_O_B

        if account_number == 0:
            self.account_number = self.generate_account_number()
        else:
            self.account_number = account_number
        
        #self.account_number = self.generate_account_number() if account_number == 0 else account_number
        self.transactions = transactions
        self.balance = balance

    @staticmethod
    def generate_account_number():
        return random.randint(1000000000, 9999999999)

    def send_money(self, account_name, account_number, bank_name, amount):
        """
        Theis method debits customer balance and sends to account numbr provided.
        Returns boolean to indicate success or failure of transaction.
        """
        if self.balance > amount:
            new_transaction = Transactions("TRANSFER","STARTED")
            new_transaction.details = {
                "bank name": bank_name,
                "account_name": account_name,
                "account number": account_number,
                "amount": amount
            }
            self.balance -= amount #same as self.balance = self.balance - amount
            self.transactions[new_transaction.date] = new_transaction.type


    def buy_airtime(self):
        pass

    def make_payments(self):
        pass

    def deposit_cash(self):
        pass

    def print(self):
        return self.__dict__