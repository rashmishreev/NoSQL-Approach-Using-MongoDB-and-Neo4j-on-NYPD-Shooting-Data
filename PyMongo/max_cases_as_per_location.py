import pymongo
from bson import objectid

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

loc = collection0.aggregate([
    {"$group" : {
        "_id": "$BORO",
        "count": { "$sum": 1 } }
    },
    {"$match": {
        "_id": {"$ne" : None },
        "count" : {"$gt": 1} }
    },
    {
        "$sort" : { "count" : -1 }
    },
    {
        "$limit": 1
    }
])
for i in loc:
    print(i)
