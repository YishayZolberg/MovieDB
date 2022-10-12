import EHAB
from pymongo import MongoClient
from fastapi import FastAPI
from pymongo.server_api import ServerApi

"""client = pymongo.MongoClient("mongodb://ehab1:ehab1994@10.0.0.12/atlascluster.wtiyv9t.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)
mydb = client["posters"]
mycol = mydb["ehab"]

mydict = { "name": "John", "address": "Highway 37" }
mydb.mycol.insert_one(mydict)
#print(x)
"""

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.database

# Created or Switched to collection names: my_gfg_collection
collection = db.p
print(collection)
mydict = {"name": "John", "address": "Highway 37"}
emp_rec1 = {
    "name": "Mr.Geek",
    "eid": 24,
    "location": "delhi"
}

rec_id1 = collection.insert_one(mydict)
# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)
