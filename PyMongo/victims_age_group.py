import pymongo
from bson import objectid
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

loc = collection0.aggregate([
    {"$unwind": "$VIC_AGE_GROUP"},
    {"$group" : {
        "_id": "$VIC_AGE_GROUP",
        "Most targeted Victim Age Group": { "$sum": 1 } }
    },
    {"$match": {
        "_id": {"$ne" : None },
        "Most targeted Victim Age Group" : {"$gt": 1} }
    },
    {
        "$sort" : { "Most targeted Victim Age Group" : -1 }
    },
    {
        "$limit": 1
    }
])
for i in loc:
    print(i)
