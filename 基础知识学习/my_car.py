from car import Car #导入模块下的类
import electric_car #导入整个模块
from collections import OrderedDict

my_car = Car("audi","a9",2019)
my_car.set_odometer(1000)
print(my_car.read_odometer())
my_car.fill_gas(999)


electric_car = electric_car.ElectricCar("audi","a8",3011)
electric_car.electric_run(10000)
electric_car.set_odometer(100)
print(electric_car.read_odometer())
electric_car.fill_gas(999)

languages = OrderedDict()
languages['jen'] = 'python'
languages['sarah'] = 'c'
languages['oliver'] = 'ruby'
languages['lee'] = 'python'

print(languages)
