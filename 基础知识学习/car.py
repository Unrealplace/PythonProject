""" 一个用于描述汽车的类 """
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

