import json
numbers = list(range(1,100))
file_name = "numbers.json"

try:
	with open(file_name,'a') as file_obj:
		json.dump(numbers,file_obj)
	pass
except Exception:
	print("发生了异常了")
	pass