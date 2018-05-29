class Dog():

	"""docstring for Dog"""
	def __init__(self, name,age):
		super(Dog, self).__init__()
		self.name = name
		self.age  = age
		
	def sit(self):
		print(self.name.title() + " is now sitting")
		pass

	def roll_over(self):
		print(self.name.title() + " is rolling over")
		pass


class Car():

	"""docstring for Car"""
	def __init__(self,make,model,year):
		super(Car, self).__init__()
		self.odometer_reading = 0
		self.make = make
		self.model = model
		self.year = year
		self.gas  = 0


	def read_odometer(self):
		return self.odometer_reading


	def set_odometer(self,meter):
		self.odometer_reading += meter

	def fill_gas(self,gas):
		self.gas = gas
		print("加油--"+str(self.gas))
		pass


# 编写个电车继承自Car
class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self,make,model,year):
		super(ElectricCar, self).__init__(make,model,year)
		self.battery_size = 8000

    # 子类新增的方法
	def electric_run(self,speed):
		print(self.model + "run with speed:" + str(speed))
		pass

    #从写父类的方法
	def set_odometer(self,meter):
		self.odometer_reading+=meter
		self.odometer_reading*=2
		pass

	def fill_gas(self,electric):
		self.battery_size = electric
		print("充电--"+str(self.battery_size))
		pass



#编写一个类并测试调用
my_dog = Dog("haha",14)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("your",111)
print("name "+your_dog.name+" age "+str(your_dog.age))

my_car = Car("Audi","a6",2018)
my_car.set_odometer(1000)
print(my_car.read_odometer())
my_car.fill_gas(1000)

#子类对象
electric_car = ElectricCar("AUDI","A9",3033)
electric_car.electric_run(10000)
electric_car.set_odometer(100)
print(electric_car.read_odometer())
electric_car.fill_gas(999)


