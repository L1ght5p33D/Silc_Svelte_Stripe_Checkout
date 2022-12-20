


from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

print("connect localhost mongo client 27017")
#client = MongoClient('localhost', 37017)

print("get test db ..")
db = client["sca_dev"]

print("found db ~ " + str( db ))
#found db ~ Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'dpm_test1')


col = db["sc_ma_test"]
#mydict = { "name": "John", "address": "Highway 37" }
#x = mycol.insert_one(mydict)

print("found collll ~ " + str(col))

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
#for item in query:
#    print("item found ~ " + item)
