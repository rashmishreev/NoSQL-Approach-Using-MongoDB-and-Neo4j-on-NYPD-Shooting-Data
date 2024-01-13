import pymongo
from bson import objectid
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

# total count of perpetrators who were male
sex_count_M = collection0.count_documents({"PERP_SEX": "M"})
print("total count of perpetrators who were male")
print (sex_count_M)

# total count of perpetrator who were female
sex_count_F = collection0.count_documents({"PERP_SEX": "F"})
print("total count of perpetrator who were female")
print (sex_count_F)

