import pymongo
from bson import objectid
from pymongo import MongoClient
import datetime


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nycDb"]
collection0 = db["nypdIncidentCol"]
print(db)
print("Mongo DB connected")



# def insert_record (data):
#    document = nypdIncidentCol.insert_one(data)
#   return document.inserted id

#DB name: nycDb
#Collection name: nypdIncidentCol



# data = {
#         "INCIDENT_KEY": "227972961",
#         "OCCUR_DATE": (5/9/21),
#         "OCCUR_TIME": "2:50:00",
#         "BORO": "BRONX",
#         "PRECINCT": 41,
#         "JURISDICTION_CODE": 2,
#         "LOCATION_DESC": "MULTI DWELL - PUBLIC HOUS",
#         "STATISTICAL_MURDER_FLAG": True,
#         "PERP_AGE_GROUP": "25-44",
#         "PERP_SEX": "F",
#         "PERP_RACE": "BLACK",
#         "VIC_AGE_GROUP": "25-44",
#         "VIC_SEX": "M",
#         "VIC_RACE": "BLACK HISPANIC",
#         "X_COORD_CD": "1014642.0",
#         "Y_COORD_CD": "240068.0",
#         "Latitude": "40.82556269",
#         "Longitude": "-73.89018729",
#         "Lon_Lat": "POINT (-73.89018728699995 40.82556269400004)"
#     }

# data = {
#         "INCIDENT_KEY":{"$numberInt":"202392895"},
#         "OCCUR_DATE":"3/10/21",
#         "OCCUR_TIME":"7:30:00",
#         "BORO":"MANHATTAN",
#         "PRECINCT":{"$numberInt":"28"},
#         "JURISDICTION_CODE":{"$numberInt":"0"},
#         "LOCATION_DESC":"MULTI DWELL - APT BUILD",
#         "STATISTICAL_MURDER_FLAG":False,
#         "PERP_AGE_GROUP":"25-44",
#         "PERP_SEX":"M",
#         "PERP_RACE":"BLACK",
#         "VIC_AGE_GROUP":"18-24",
#         "VIC_SEX":"M",
#         "VIC_RACE":"BLACK",
#         "X_COORD_CD":{"$numberDouble":"998054.0"},
#         "Y_COORD_CD":{"$numberDouble":"232172.0"},
#         "Latitude":{"$numberDouble":"40.80393188"},
#         "Longitude":{"$numberDouble":"-73.95014024"},
#         "Lon_Lat":"POINT (-73.95014024399995 40.80393187900006)"}

#read

#
# insert_cursor = col.insert_one(data)
#
# print(insert_cursor)
#
