
from pymongo import MongoClient
import json
from silc_auth_api.check_auth import check_un_exists, check_em_exists


	
def create_account(pd):
	print("connect mongo client")                                                                                                                                        
	client = MongoClient('mongodb://localhost:27017/')
	db= client["sca_dev"]
	user_col = db["silc_users_0"]
	print("Decode post to insert")
	pdjl = json.loads(pd)
	pdjls = str(pdjl)
	print("get pd load str" + pdjls)
	print("get user for PRIV checkauth")

	b_ins_acc = \
     {"uName":"init_name",
	 "uEmail":"init_email",  \
     "uKey":"init_key" \
      }

	kc = 0
	for k,v in pdjl.items():
		print("get json k,v wise ~ key ~ " + str(k) + " val ~ " + str(v))
	
	for k,v in pdjl.items():
		print("check for uname key")
		if k == "uname":
			print("check post data key items found uname ~ " + str(v))
			b_ins_acc["uName"] = v
			print("chk len uname and key ~")
			if len(v) > 88:
				print("username too long")
				return "username too long"
			
			r_uname = v
			print("register posted uname ~" + str( r_uname ))
			user_exists = check_un_exists( r_uname )
			if user_exists == True:
				print("User already exists.. return register fail")
				return "username already exists"
			if user_exists == False:
				print("Username not found.. continue reg and insert")

			#auc = user_col.find(ufq)
			#print("auth uname check ~ " + str( auc ))
			#ct_names = 0
			#for k in auc:
			#    ct_names +=1
			#    print("loop auth unames ~ " + str(k))
			#if ct_names > 0:
			#    print("found existing username")
			#    return "fail"
		print("pass name key check email")
		if k == "email":
			print("check post data key items found email ~" + str(v))
			
			email_exists = check_em_exists( v )

			if email_exists == True:
				print("email already exists return register fail")
				return "email already exists"
			if email_exists == False:
				print("email not found continue reg and insert")
			b_ins_acc["uEmail"] = v
			# b_ins_acc["uEmail"] = pdjl["email"]	
		print("pass email check key")
		if k == "key":
			print("check post data key items found user key ~ " + str(v))
			b_ins_acc["ukey"] = v
			# b_ins_acc["ukey"] = pdjl["key"]
			# Dev master pass for testing. delete later remove for prod
			# if v == "create_pass":
				# b_ins_acc["uKey"] = "HASHPASS"
	print("check bins for input ~ " + str(b_ins_acc))
	if b_ins_acc["uEmail"] != "init_email" and \
		b_ins_acc["uName"] != "init_name" :
		mir = user_col.insert_one(b_ins_acc)
		print("mongo insert write result ~ " + str( mir ))
		print("create_account success return true")
		return "success"
	else:
		print("account create failed return fail(shouldnt get here)")
		return "create account failed"
		#user_col.insert_one(json.loads(pd))
		# not work from json post fetch
		# pdla = []
		# for char in str(pdl).encode("ascii"):
		#     pdla.append(char)
		# print("ORD pd s ~ " + str(pdla))
		# print("len ord s ~ " + str(len(pdla)))
		
		
		# pds = json.loads(str(json.loads(pd)))
		# print("get pd json loads str ~ " + str(pds))

		# pdsa = []
		# for char in str(pds).encode("ascii"):
		#     pdsa.append(char)
		# print("ORD pd s ~ " + str(pdsa))
		# print("len ord s ~ " + str(len(pdsa)))

		#user_col.insert_one(pds)
