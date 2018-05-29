import pizza_module
from cake_module import make_buffer_cake,make_cake as mk
import person_module as pm 

def greet_user():
	"""显示简单的问候语 """
	print("hello")
	pass

greet_user()

# 向函数传递参数
def greet_user(message):
	print("hello " +message.title())
	pass
greet_user("liyang")

# 传递的是值 和 穿引用有区别，内部不能改变外部的值 
def describe_pet(animal_type,pet_name):
	print(animal_type+"name:"+pet_name)
	animal_type = "hello world"
	pass

animal_type = "英国短腿狗"
pet_name = "小马"
describe_pet(animal_type,pet_name)
print(animal_type)


#关键字实参，类似于java 中防止参数输入错误
describe_pet(animal_type="Dog",pet_name="🐶")


#行参默认值
def describe_pet(animal_type,pet_name="阿猫阿狗"):
	print(animal_type+"name:"+pet_name)
	animal_type = "hello world"
	pass

describe_pet(animal_type="日本人")
describe_pet(animal_type="美国人",pet_name="狗狗")


# 实参变的可选
def formate_name(first_name,last_name,middle_name=''):
	if middle_name:
		return first_name.title() +middle_name.title() + last_name.title()
		pass
	else:
		return first_name.title() + last_name.title()
	pass

joke = formate_name('joke','lee')
peter = formate_name('peter','maa','jhon')
print(joke+'\n')
print(peter)

# 返回字典
def build_person(first_name,last_name,age=''):
	person = {  'first':first_name,
	 			'last':last_name
				}
	if age:
		person['age']=age
		pass

	return person
	pass

person = build_person('liyang','lee',27)
print(person)

#传递列表 ,列表传递的是引用进来，
def hello_person(persons):
	for person in persons:
		message = "hello " + person.title() + "nice to meet you!\n"
		person = "yyyyyy" #这种修改对外部没有用，相当于创建了一个新的变量
		print(message)
		pass
	persons[0]="0000000" #这样在函数内部修改会影响外部
	pass

persons = ["liyang","oliver","jhon"]
hello_person(persons)
print(persons)

# 防止函数修改外部的列表内容
print("***传递副本列表的copy****")
persons = ["liyang","oliver","jhon"]
hello_person(persons[:])
print(persons)


# 传递任意数量的实参数,函数会包装一个空的元祖，然后将参数方进去
def make_pizza(*params):
    if params:
    	print(params)

make_pizza("water","buffer")
make_pizza("water")
make_pizza()

# 使用位置实参，和任意数量的实参
def make_pizza(size,*params):
	for param in params:
		print(param)
		pass
	print("\n"+"pizza size :"+str(size))
	pass

make_pizza(14,"水","面","肉")

# 使用位置实参，和任意数量的关键字实参,相当于键值对的形式，包装到字典中 
def build_profile(first_name,last_name,**user_info):
	profile = {}
	profile['first'] = first_name
	profile['last']  = last_name
	for key,value in user_info.items():
		profile[key] = value
		pass
	return profile


usr_profile = build_profile('li','yang',age="27",love="girl")
print(usr_profile)

#通过模块调用外部函数
pizza_module.module_make_pizza(15,"面","糖")
#导入特定的函数
make_buffer_cake(111)
#导入函数的时候通过as 区别名，用来区分和当前文件中的函数万一有冲突
mk(1888)
#给模块取别名，方便调用内部的函数
pm.make_person()


