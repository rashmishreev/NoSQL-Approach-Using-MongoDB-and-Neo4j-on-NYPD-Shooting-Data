import pymongo
from bson import objectid
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

# Perpetrators Ethnicities
perpetrators_race = collection0.distinct("PERP_RACE")
print("Perpetrators Ethnicities")
print(perpetrators_race)

# Count of Perpetrators Ethnicities
count_AIN = collection0.count_documents({"PERP_RACE": "AMERICAN INDIAN/ALASKAN NATIVE"})
count_AP = collection0.count_documents({"PERP_RACE": "ASIAN / PACIFIC ISLANDER"})
count_B = collection0.count_documents({"PERP_RACE": "BLACK"})
count_BH = collection0.count_documents({"PERP_RACE": "BLACK HISPANIC"})
count_U = collection0.count_documents({"PERP_RACE": "UNKNOWN"})
count_W = collection0.count_documents({"PERP_RACE": "WHITE"})
count_WH = collection0.count_documents({"PERP_RACE": "WHITE HISPANIC"})

print("\n Count of Perpetrators Ethnicities")

print("AMERICAN INDIAN/ALASKAN NATIVE:", count_AIN, "\n",
      "ASIAN / PACIFIC ISLANDER:", count_AP, "\n",
      "BLACK:", count_B, "\n",
      "BLACK HISPANIC:", count_BH, "\n",
      "UNKNOWN:", count_U, "\n",
      "WHITE:", count_W, "\n",
      "WHITE HISPANIC:", count_WH)
