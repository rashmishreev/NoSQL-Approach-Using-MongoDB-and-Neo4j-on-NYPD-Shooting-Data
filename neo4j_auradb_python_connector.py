# -*- coding: utf-8 -*-
"""Copy of Neo4j_AuraDB_Python_connector.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zcmy6y-PLUg-CyGaFI5n3Smy3SFmPldF
"""

!pip install neo4j
!pip install py2neo

import os

os.getcwd()

from google.colab import drive
drive.mount('/content/drive')

os.chdir(r"/content/drive/Shareddrives/DATA 225/Assignments 13%/HW 4/Neo4j")
os.listdir()

import pandas as pd
df= pd.read_csv("../NYPD_Shooting_Incident_Data__Historic_ cleaned.csv")
df.shape

df.info()

# there are 4 key entities: incidents, victims, perpetrators, locations.
# we need a unique identifier for all entities to link them to incident in our graph solution.
# however, the database does not support unique IDs for victims, perpetrators.
# unique location can be identified by Lon_Lat
# we will create it.

# some facts:
# 1. each row represents a victim uniquely
# 2. each incident key identifies an incident uniquely
# 3. an incident has 1/more victims
# 4. an incident has 1/more perpetrators
# 5. an incident has 1 unique location
# 6. an incident has 1 unique event timestamp

df['Lon_Lat'].value_counts()

df['INCIDENT_KEY'].value_counts()

df.head()

df.reset_index(inplace=True)
df.rename(columns={"index":'VICTIM_ID'}, inplace=True)
df.head()

a= df['INCIDENT_KEY'].value_counts().reset_index()
a.columns=['INCIDENT_KEY', 'cnt']
a

import numpy as np
conditions  = [ a['cnt'] == 1, a['cnt']>1 ]
choices     = [ "no", 'yes']
a["MASS_SHOOTING"] = np.select(conditions, choices, default=np.nan)
a

a.drop(columns='cnt', inplace=True)
a

df= pd.merge(df, a, left_on='INCIDENT_KEY', right_on='INCIDENT_KEY', how='left')
df

df.columns

df.info()

#df['PERP_ID']= df.set_index(['brand','description']).index.factorize()[0]+1
df.set_index(['PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'INCIDENT_KEY']).index.factorize()[0]+1

df.insert(loc=0, column='PERP_ID', value=df.set_index(['PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'INCIDENT_KEY']).index.factorize()[0]+1)
df

a= df[['PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'INCIDENT_KEY']].value_counts().reset_index()
a

a['INCIDENT_KEY'].value_counts()

a[a['INCIDENT_KEY']==231246225]

df[df['INCIDENT_KEY']==231246225][['PERP_ID', 'VICTIM_ID', 'INCIDENT_KEY', 'OCCUR_DATE', 'OCCUR_TIME',
       'BORO', 'PRECINCT', 'STATISTICAL_MURDER_FLAG', 'PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE',
       'VIC_AGE_GROUP', 'VIC_SEX', 'VIC_RACE']]

df.info()

df.to_csv('NYPD_ShootingData_CLEAN.csv', index=False)

"""# Create Nodes"""

import json
from py2neo import Graph
from py2neo.bulk import create_nodes, create_relationships
from py2neo.data import spatial

df.columns

# prepare INCIDENT node data
dfi = df.filter(["INCIDENT_KEY", 'OCCUR_DATE', 'OCCUR_TIME'])
dfi = dfi.drop_duplicates(keep='last')
json_i = dfi.to_json(orient="records")
dict_i = json.loads(json_i)
len(dict_i)

# prepare Mass shooting node data
dfms = df.filter(['MASS_SHOOTING'])
dfms.drop_duplicates(keep='last', inplace=True)
json_ms = dfms.to_json(orient="records")
dict_ms = json.loads(json_ms)
len(dict_ms)

dict_ms

# prepare location node data
dfl = df.filter(['Lon_Lat', 'X_COORD_CD', 'Y_COORD_CD', 'Latitude', 'Longitude'])
dfl.drop_duplicates(keep='last', inplace=True)
json_l = dfl.to_json(orient="records")
dict_l = json.loads(json_l)
len(dict_l)

# prepare jur node data
dfj = df.filter(['JURISDICTION_CODE'])
dfj.drop_duplicates(keep='last', inplace=True)
json_j = dfj.to_json(orient="records")
dict_j = json.loads(json_j)
len(dict_j)

dict_j

# prepare boro node data
dfb = df.filter(['BORO'])
dfb.drop_duplicates(keep='last', inplace=True)
json_b = dfb.to_json(orient="records")
dict_b = json.loads(json_b)
len(dict_b)

dict_b

# prepare locdesc node data
dfld = df.filter(['LOCATION_DESC'])
dfld.drop_duplicates(keep='last', inplace=True)
json_ld = dfld.to_json(orient="records")
dict_ld = json.loads(json_ld)
len(dict_ld)

dict_ld

df.columns

# prepare Victim node data
dfv = df.filter(["VICTIM_ID", 'VIC_AGE_GROUP', 'VIC_SEX', 'VIC_RACE'])
dfv = dfv.drop_duplicates(keep='last')
json_v = dfv.to_json(orient="records")
dict_v = json.loads(json_v)
len(dict_v)

# prepare murderflag node data
dfmf = df.filter(['STATISTICAL_MURDER_FLAG'])
dfmf.drop_duplicates(keep='last', inplace=True)
json_mf = dfmf.to_json(orient="records")
dict_mf = json.loads(json_mf)
len(dict_mf)

# prepare Perp node data
dfp = df.filter(['PERP_ID','PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE'])
dfp = dfp.drop_duplicates(keep='last')
json_p = dfp.to_json(orient="records")
dict_p = json.loads(json_p)
len(dict_p)

# Commented out IPython magic to ensure Python compatibility.
# %who

del a, dfb,	 dfi,	 dfj,	 dfl,	 dfld,	 dfmf,	 dfms,	 dfp,	 dfv 
del json_b,	 json_i,	 json_j	, json_l	, json_ld	 ,json_mf	 ,json_ms	, json_p,	 json_v

# Commented out IPython magic to ensure Python compatibility.
# %who

# dict_i	 dict_ms	 
# dict_l dict_j dict_b dict_ld
# dict_p
# dict_v dict_mf

"""# Add Nodes"""

graph = Graph("neo4j+s://e86020ea.databases.neo4j.io", auth=("neo4j", "auth_key"))
graph

# Create nodes
create_nodes(graph.auto(), dict_i, labels={"Incident"})
print(graph.nodes.match("Incident").count())

create_nodes(graph.auto(), dict_ms, labels={"MassShooting"})
print(graph.nodes.match("MassShooting").count())

create_nodes(graph.auto(), dict_l, labels={"location"})
print(graph.nodes.match("location").count())

create_nodes(graph.auto(), dict_j, labels={"Jurisdiction"})
print(graph.nodes.match("Jurisdiction").count())

create_nodes(graph.auto(), dict_b, labels={"BORO"})
print(graph.nodes.match("BORO").count())

create_nodes(graph.auto(), dict_ld, labels={"LOCATION_DESC"})
print(graph.nodes.match("LOCATION_DESC").count())

create_nodes(graph.auto(), dict_v, labels={"victim"})
print(graph.nodes.match("victim").count())

create_nodes(graph.auto(), dict_p, labels={"perpetrator"})
print(graph.nodes.match("perpetrator").count())

"""# prepare relationships"""

df_rel = df.filter(["INCIDENT_KEY", "VICTIM_ID"])
json_rel = df_rel.to_json(orient="records")
dict_rel_v = json.loads(json_rel)

#create relationships incidents involving victims
ex_victim = []

for p in dict_rel_v:
    incident= p["INCIDENT_KEY"]
    victim = p["VICTIM_ID"]
    ex_victim.append((incident,{'involves_v':1},victim))

print(ex_victim)

rel_iv = create_relationships(graph.auto(), 
                              ex_victim, 
                              "INVOLVES_V", 
                              start_node_key=("Incident", "INCIDENT_KEY"), 
                              end_node_key=("victim", "VICTIM_ID"))
print(rel_iv)

"""# SIMILARLY WE CAN DEFINE OTHER RELATIONSHIPS

# Query DATA
"""

test = graph.run("""MATCH (n1:Incident)-[r:IS]->(n2:Mass_shooting) RETURN r, n1, n2 LIMIT 25""").data()
test

