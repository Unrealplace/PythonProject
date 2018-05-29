from car import Car
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