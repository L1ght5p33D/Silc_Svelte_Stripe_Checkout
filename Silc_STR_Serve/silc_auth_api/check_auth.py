


from pymongo import MongoClient
import json

import copy

def san_lstr(s):
	#Todo look asci only
	#string safe
	ss=True
	if len(s) > 88:
		ss=False
	if "\\" in s:
		ss=False
	if "/" in s:
		ss=False
	return ss


def check_auth(post_data):
	print("check_auth called ~")
	client = MongoClient('mongodb://localhost:27017/')
	db= client["sca_dev"]
	user_col = db["silc_users_0"]

	print("get post data str ~ " + str(post_data))
	pdjl = "other_type"
	try:
		pdjl = json.loads(post_data.decode())
		# pdjl = json.loads(post_data.decode("utf-8"))
	except Exception as err:
		print("Catch json decode err ~ ")
		print("pstring ~ " + str(post_data))
	if pdjl == "other_type":
		print("not auth other type check auth req")
		return "fail"
	un="not auth uname"
	try:
		un = pdjl["uname"]
	except Exception as err:
		print("uname not in auth err " + str(err) )
		return "fail"
	
	ky = pdjl["key"]
	print("Get un" + str(un))
	if san_lstr(un) == False:
		return "fail"
	if san_lstr(ky) == False:
		return "fail"

	# Find user/key = not found 
	fu = "nf"
	fk = "nf"
	cfu = user_col.find({"uName": un })
	ct_names = 0
	for k in cfu:
		ct_names +=1
	if ct_names < 1:
		print(" un not found fail")
		return "fail"
	if ct_names == 1:
		print("found single user ~ " + k)
		fu = k    
	
	cfk = user_col.find({"uKey": "HASHPASS"})
	for k in cfk:
		ct_ks +=1
	if ct_ks < 1:
		print(" un not found fail")
		return "fail"
	if ct_ks == 1:
		print("found single user key~ " + k)
		fk = k

	print("found user u k ~ " + str(u) + " ~ " + str(k))
	return "success"


def check_un_exists(un):
	print("call check_un_exists ~ ")
	client = MongoClient('mongodb://localhost:27017/')
	db= client["sca_dev"]
	user_col = db["silc_users_0"]


	tcf = user_col.find({"uName": un })
	
	c_names= 0
	for k in tcf:
		c_names += 1
		print("looping pymongo res cursor ~ ")
		print(str(k))


	print("counted names res 0 ~ " + str(c_names))
	
	if c_names > 0:
		print("found existing username")
		return True
	else:
		print("User not found")
		return False


def check_em_exists(em):
	print("call check_em_exists ~ ")
	client = MongoClient('mongodb://localhost:27017/')
	print("mdb con succ")
	db= client["sca_dev"]
	user_col = db["silc_users_0"]


	tcf = user_col.find({"uEmail": em })
	
	c_names= 0
	for k in tcf:
		c_names += 1
		print("looping pymongo res cursor ~ ")
		print(str(k))


	print("counted names res 0 ~ " + str(c_names))
	
	if c_names > 0:
		print("found existing email")
		return True
	else:
		print("email not found")
		return False