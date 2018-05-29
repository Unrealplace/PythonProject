# 获取用户输入的文本
name = input("please input your name:\n")
print("your name is :"+str(name))

# 将用户输入转化成int类型
age = input("please input your age\n")
age = int(age)

if age >= 20 and age <=30:
	print("你是一个青年人了！")
	pass


# 用while 来进行循环
active = True
while active:
	message = input("please input promot\n")
	if message == "quit":
		# active = False
		break
		pass
	else:
		print(message)
	pass

# break 退出循环

active = True
while active:
	for x in range(1,1000):
		if x >= 555:
			active = False
			pass
		else:
			print(x)
		pass

	pass


# 通过字典来存储信息
responses = {}
polling_active = True
while polling_active:
	name = input("what is your name\n")
	response = input("what mountain would you like to climb someday?\n")
	responses[name] = response

	repeat = input("would you like to let another person response?(YES/NO)")
	if repeat == 'YES' or repeat == 'Y':
		polling_active = True
		pass
	else:
		polling_active = False

	print("The results:\n")

	for key,value in responses.items():
		print(key+" want to climb "+value)
		pass
	pass
