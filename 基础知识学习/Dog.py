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