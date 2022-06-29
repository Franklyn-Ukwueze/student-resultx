import random 
from transactions import Transactions

class Customer:
    def __init__(self, name, phone_number,
     gender, date_of_birth, account_number=0, transactions={}, balance=0):
        """
        create customer, ensure to add name, phone number, gender and date of birth.
        System will generate acccount number
        """
        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.date_of_birth = date_of_birth

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

    def send_money(self, receiver_name, receiver_account_number, receiver_bank, amount):
        """
        This method debits customer balance and sends to account number provided.
        Returns boolean to indicate success or failure of transaction.
        """
        if self.balance > amount:
            new_transaction = Transactions("TRANSFER","STARTED")
            new_transaction.details = {
                "bank_name": receiver_bank,
                "account_name": receiver_name,
                "account_number": receiver_account_number,
                "amount": amount
            }
            self.balance -= amount #same as self.balance = self.balance - amount
            self.transactions[new_transaction.date] = new_transaction.description


    def buy_airtime(self, network, phone_number, airtime_type, amount):
        """
        This method debits customer balance and purchases  airtime for the phone number provided.
        """
        if self.balance > amount:
            new_transaction = Transactions("AIRTIME PURCHASE","STARTED")
            new_transaction.details = {
                "service_provider": network,
                "amount": amount,
                "phone_number": phone_number,
                "type": airtime_type
            }
            self.balance -= amount
            self.transactions[new_transaction.date] = new_transaction.description

    def make_payments(self, payment_destination, payment_ref, amount):
        """
        This method debits customer account and sends money to the paymet detination provided
        """
        if self.balance > amount:
            new_transaction = Transactions("PAYMENT", "STARTED")
            new_transaction.details = {
                "payment_detination": payment_destination,
                "payment_reference": payment_ref,
                "amount": amount
            }        
            self.balance -= amount
            self.transactions[new_transaction.date] = new_transaction.description

    def deposit_cash(self, depositor_name, depositor_phone_number, amount):
        """
        This method credits customer account when it receives a transfer request from another account
        """
        if amount > 0:
            new_transaction = Transactions("CREDIT", "SUCCESSFUL")
            new_transaction.details ={
                "depositor_name": depositor_name,
                "depositor_phone number": depositor_phone_number,
                "amount": amount 
            }
            self.balance += amount
            self.transactions[new_transaction.date] = new_transaction.description
        

    def print(self):
        return self.__dict__