import pymongo
from bson import objectid
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

result = collection0.find().sort("BORO", -1)

for i in result:
        print (i)
