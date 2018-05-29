#意思是从 0 开始数知道数够10个数
for value in range(0,10):
	print(value)
	pass


#rang 转换 list
numbers = list(range(0,16))
print(numbers)

#指定步长
numbers = list(range(0,20,2))
print(numbers)

#获取平方数
squares = []
for value in range(1,10):
	squares.append(value**2)
	pass
print(squares)

#统计计算
print("max--"+str(max(squares)))
print("min--"+str(min(squares)))
print("sum--"+str(sum(squares)))

#更简单的获取列表
squares = [value**3 for value in range(1,10)]
print(squares)

print("**************")
#进行切片操作
slice_arr = squares[:3]
print(slice_arr)
slice_arr = squares[0:3]
print(slice_arr)
#切片操作超过范围后全部取出
slice_arr = squares[1:11]
print(slice_arr)
slice_arr = squares[2:]
print(slice_arr)
slice_arr = squares[-3:]
print(slice_arr)
slice_arr = squares[-100:-1]
print(slice_arr)

#复制一个切片
slice_arr = squares[:]
print(slice_arr)

#指向同一个内存
slice_arr_a = slice_arr
print(slice_arr_a)
slice_arr_a[0]="hello"
print(slice_arr)

#产生了新的对象了
slice_arr_b = slice_arr_a[:]
slice_arr_b[1]="change"
print(slice_arr)




