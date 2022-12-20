

def login_post_handler( pdata ):
	print(  "post data pass to handler ~ " + str(pdata) )


	# Lookup if user exists by email from mongo

	# If not exist return "UserNotFound"
	return {"login_stat": "UserNotFound" }

	# If user exists, confirm password  is exact match return "UserFound"




