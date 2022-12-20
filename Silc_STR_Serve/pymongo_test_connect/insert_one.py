


from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

print("connect localhost mongo client 27017")
#client = MongoClient('localhost', 37017)

print("get test db ..")
db = client["sca_dev"]

print("found db ~ " + str( db ))
#found db ~ Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'dpm_test1')


col = db["products"]
#mydict = { "name": "John", "address": "Highway 37" }
#x = mycol.insert_one(mydict)

print("found collll ~ " + str(col))

col.insert_one({"ins from pymongo":"ins0"})


