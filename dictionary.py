
alien_list = ["hello","world","nice"]

dic = {
        "age":111,
		"name":"oliver lee"
		}

alien0 = {
		"color":"Red",
		"age":100,
		"points":122,
		"alien":alien_list,
		"dic":dic
		}

print(alien0)

#访问字典中的元素
print(alien0["dic"])


#添加键值对
alien0["name"] = "alien"
alien0["time"] = "12:30"
print(alien0)

print("*************")
#申明空字典
empty_dic = {}
empty_dic["age"]=100
empty_dic["name"]="oliver"
print(empty_dic)


#修改字典中的值
empty_dic["age"] = 101010
print(empty_dic)

#删除键值对
del (alien0["dic"])
print(alien0)

for key,value in alien0.items():
	print("key--->"+str(key))
	print("value--->"+str(value))
	pass

print("***********")
for key in alien0.keys():
	print(key)
	pass

for values in alien0.values():
	print(values)
	pass

