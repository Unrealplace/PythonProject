import json
file_name = "numbers.json"

try:	
	with open(file_name,'r') as file_obj:
		numbers = json.load(file_obj)
	pass
except Exception as e:
	print("发生了异常了")
	pass
else:
	print(numbers)