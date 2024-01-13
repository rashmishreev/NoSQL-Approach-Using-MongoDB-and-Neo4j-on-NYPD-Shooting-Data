import pymongo
from bson import objectid
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

myquery = {"VIC_SEX": {"$regex": "^M"}}
result = collection0.find(myquery)

for i in result:
        print (i)
