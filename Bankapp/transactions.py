import datetime


class Transactions:
    def __init__(self, type, status):
        """
        This records the date, type, staus and details
        of all the transactions made by the customer
        """   
        self.date = datetime.datetime
        self.type = type
        self.status = status
        self.details = {}

    def  print(self):
        return self.__dict__