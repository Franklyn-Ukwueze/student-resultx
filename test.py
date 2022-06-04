import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(myclient.list_database_names()) 

print(mydb.list_collection_names())