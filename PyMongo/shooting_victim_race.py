import pymongo
from bson import objectid
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

# Ethnicities impacted by shooting
victim_race = collection0.distinct("VIC_RACE")
print("Ethnicities impacted by shooting")
print(victim_race)

# count of individual ethnicities impacted
count_AIN = collection0.count_documents({"VIC_RACE": "AMERICAN INDIAN/ALASKAN NATIVE"})
count_AP = collection0.count_documents({"VIC_RACE": "ASIAN / PACIFIC ISLANDER"})
count_B = collection0.count_documents({"VIC_RACE": "BLACK"})
count_BH = collection0.count_documents({"VIC_RACE": "BLACK HISPANIC"})
count_U = collection0.count_documents({"VIC_RACE": "UNKNOWN"})
count_W = collection0.count_documents({"VIC_RACE": "WHITE"})
count_WH = collection0.count_documents({"VIC_RACE": "WHITE HISPANIC"})

print("count of individual ethnicities impacted")

print("AMERICAN INDIAN/ALASKAN NATIVE:", count_AIN)
print("ASIAN / PACIFIC ISLANDER:", count_AP, "\n",
      "BLACK:", count_B, "\n",
      "BLACK HISPANIC:", count_BH, "\n",
      "UNKNOWN:", count_U, "\n",
      "WHITE:", count_W, "\n",
      "WHITE HISPANIC:", count_WH)
