class Transactions:
    def __init__(client, date, type, status, details):
        """
        This records the date, type, staus and details
        of all the transactions made by the customer
        """   
        client.date = date
        client.type = type
        client.status = status
        client.details = {}

    def  print(client):
        return client.__dict__