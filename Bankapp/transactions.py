import datetime


class Transactions:
    def __init__(self, description, status):
        """
        This records the date, type, staus and details
        of all the transactions made by the customer
        """   
        self.date = str(datetime.datetime)
        self.description = description
        self.status = status
        self.details = {}

    def  print(self):
        return self.__dict__