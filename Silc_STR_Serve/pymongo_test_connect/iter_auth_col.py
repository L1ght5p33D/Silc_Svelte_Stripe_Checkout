


from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

print("connect localhost mongo client 27017")
#client = MongoClient('localhost', 37017)

print("use client sca dev")
db = client["sca_dev"]

print("found db ~ " + str( db ))

col = db["userAuth"]

print("found user auth col ~ " + str(col))

# not work
#print("col find ~ " + pprint((col.find_one())))

print("get db list coll " )
cnames = db.collection_names()

for c in cnames:
    print("found col ~" + str( c )) 

print("get col names ~ " + str( cnames ))

print("query")
query = col.find_one({})

print( "qq" + str(query) )

lquery = col.find({"sp_uname":"create_un"})
for item in lquery:
    print("list query item found ~ " + str(item))
