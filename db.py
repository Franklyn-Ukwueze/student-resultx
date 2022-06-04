import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["med_data"]
my_collection = db["patient_data"]

patient_record = {
    "Name": "Maureen Whoever",
    "Age": 29,
    "Gender": "Female",
    "BP": [{"sys": 156}, {"dia": 82}],
    "Heart rate": 82
}

my_collection.insert_one(patient_record)

for item in my_collection.find():
    pprint(type(item))