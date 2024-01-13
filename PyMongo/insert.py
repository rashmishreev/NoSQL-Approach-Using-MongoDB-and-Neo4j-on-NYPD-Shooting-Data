import pymongo
from bson import objectid

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")

data = [
    {"INCIDENT_KEY" : 3424234, "LOCATION_DESC": "CENTRAL SIGNAL", "BORO": "STATEN", "X_COORD_CD": "1014642", "Y_COORD_CD": "240021"},
    {"INCIDENT_KEY" : 4354555, "LOCATION_DESC": "SKY ST. 33", "BORO": "BROOKLYN", "X_COORD_CD": "1014632", "Y_COORD_CD": "240032"},
    {"INCIDENT_KEY" : 2131244, "LOCATION_DESC": "MUSEUM", "BORO": "STATEN", "X_COORD_CD": "1014623", "Y_COORD_CD": "240024"},
    {"INCIDENT_KEY" : 6565464, "LOCATION_DESC": "VIBE MALL", "BORO": "QUEENS", "X_COORD_CD": "1014612", "Y_COORD_CD": "240043"},
    {"INCIDENT_KEY" : 3453464, "LOCATION_DESC": "TEST LOCATION", "BORO": "BRONX", "X_COORD_CD": "1014634", "Y_COORD_CD": "240064"},
    {"INCIDENT_KEY" : 5765745, "LOCATION_DESC": "SIDE WAY 322", "BORO": "MANHATTAN", "X_COORD_CD": "1014452", "Y_COORD_CD": "240052"},
]

i = collection0.insert_many(data)
#all new IDs will be printed
print(i.inserted_ids)
