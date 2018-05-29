import json

def get_stored_username():
	file_name = "username.json"
	try:
		with open(file_name) as file_obj:
			username = json.load(file_obj)
		pass
	except Exception as e:
		return None
	else:
		return username
		pass
	pass

def get_new_username():
	username = input("what your name:\n")
	file_name = "username.json"
	with open(file_name,"w")as file_obj:
		json.dump(username,file_obj)
	return username
	pass

def greet_user():
	user_name = get_stored_username()
	if user_name:
		print("welcome back "+ user_name)
		pass
	else:
		user_name = get_new_username()
		print("i wiil remember you when you come back!")
	pass

greet_user()

