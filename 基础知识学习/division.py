file_name = "helloo.py"

try:
	print(5/0)
except ZeroDivisionError:
	print("you can't divide bu zero")

#在终端下进行操作才能输入
print("give me two numbers and i will divide them for you !\n")
print("Enter 'q' to quit .")

while True:
	first_num = input("\nFirst num:\n")
	if first_num == 'q':
		break
		pass
	second_num = input("Second num:\n")
	if second_num == 'q':
		break
		pass
	try:
		answer = int(first_num)/int(second_num)
		pass
	except Exception :
		print("发生异常了")
		break
	else:
		print(answer)
		pass
	pass

#读取的文件不存在的情况

try:
	with open(file_name) as file_obj:
		contents = file_obj.read()
except FileNotFoundError:
	msg = "sorry, the file " + file_name + "does not found"
	print(msg)


 