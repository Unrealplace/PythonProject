
arr = ['hello','world','nice to ','meet','you']
print(arr)
# for 循环遍历
for x in arr:
	print(x)
	pass

#通过下标来取列表中的元素
print(arr[0])
print(arr[-1])


#列表的增删改查操作
motor_cycles = ["honda","ymaha","suzuki"]
# 列表末尾增加一个数据
motor_cycles.append("nice to meet you")
# 修改
motor_cycles[1] = "oliverlee"
#插入元素
motor_cycles.insert(0,"liyang")
motor_cycles.insert(0,"liyang")

print(motor_cycles)




print("***************")
#删除知道位置的元素
del motor_cycles[1]
print(motor_cycles)
#从列表中pop 出数据，这个数据还可以使用,弹出最后一个元素
pop_motor = motor_cycles.pop()
print(pop_motor)
print(motor_cycles)
#弹出指定位置的元素
pop_motor = motor_cycles.pop(0)
print(pop_motor)
print("\n*********\n")
#不知道要删除的元素的位置，只知道元素
motor_cycles.remove("suzuki")
print(motor_cycles)

print("***************")

#创建一个空列表
animals = []
animals.append("dog")
animals.append("cat")
animals.append("fish")
animals.append("flower")
print(animals)

#*********永久行排序***#
#排序
animals.sort()
print(animals)
#反向排序
animals.sort(reverse=True)
print(animals)


print("***************")
#临时性排序,相当于又返回值的排序哦
new_animals = sorted(animals)
print(animals)
print(new_animals)
new_animals.reverse()
print(new_animals)

print("count"+str(len(new_animals)))








