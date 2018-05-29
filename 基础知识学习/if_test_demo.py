age = 19

age =33

if age>15 and age<25:
	print("this is a good girl")
	pass
else:
	print("this is not a good girl")


#判断某个元素是否在列表中用 in 表达式
age_list = range(10,50)
if age in age_list:
	print("age is in the list")
	pass
else:
	print("aeg is not in the list")



age = 111
if age not in age_list:
	print("age not in the list")
	pass

age = 11
if age > 15 :
	pass
elif age < 10:
	pass
else:
	print("age is in [10,15]")


age = 111
#多个elif 判断
if age < 10:
	pass
elif age < 20:
	pass
elif age < 50:
	pass
elif age < 80:
	pass
else:
	print("该死掉了哦")



