from pymongo import MongoClient
import json
from silc_auth_api.check_auth import check_auth
import time

	
	
def create_prod(pd):
	print("import pymongo")                                                                                                                                        
	client = MongoClient('mongodb://localhost:27017/')
	db= client["sca_dev"]
	user_col = db["silc_products_0"]
	print("Decode post to insert")
	'''
	Possible escape/unwanted char catching scheme leave out for now
	str(pd) -- > b ' " {
	pdo = []
	for char in str(pd).encode("ascii"):
	    pdo.append(char)
	print("ORD pd o ~ " + str(pdo))
	print("len ord o ~ " + str(len(pdo)))
	'''
	# print("get create prod pd ~ " + str(pd.decode()))
	# pdjl = json.loads(pd)
	# pdjl = json.loads(pd.decode())
	pdjl = json.loads(pd.decode())
	
	ts = round(time.time())
	bprod_insert = {"uName":"init_prod_uname",
					"ts": ts
	}
	
	print("check auth later here ... return auth fail")
	if "uname" in pdjl.keys():
			print("found prod uname ~ " + str(pdjl["uname"]))
			bprod_insert["uName"] = pdjl["uname"]
	
	print("get pdjl ~ " + str( pdjl))
	try:
		
		print("check all create prod keys ")
		if "prodname" in pdjl.keys():
			print("found prod name ~ " + str(pdjl["prodname"]))
			bprod_insert["pName"] = pdjl["prodname"]
		else:
			print("name not in ret fail")
			return "fail"
		if "proddesc" in pdjl.keys():
			print("found prod desct ~ " + str(pdjl["proddesc"]))
			bprod_insert["pDesc"] = pdjl["proddesc"]
		else:
			print("desc not in ret fail")
			return "fail"
		if "prodprice" in pdjl.keys():
			print("found prod name ~ " + str(pdjl["prodprice"]))
			bprod_insert["pPrice"] = pdjl["prodprice"]
		else:
			print("price not in ret fail")
			return "fail"
	except Exception as e:
		print("except in product data key loop")
		return "fail"

	
	print("continue to db insert")

	user_col.insert_one( bprod_insert )
	return "success"


