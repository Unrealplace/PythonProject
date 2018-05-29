
file_name = 'pi_million_digits.txt'
lines = []
with open(file_name) as file_object:
	# contents = file_object.read()
	lines = file_object.readlines()
	# print(contents)

pi_string =''
for line in lines:
	pi_string+=line.rstrip()

print(pi_string[:50] + "\nlength-->"+str(len(pi_string)))

birthday = input("please enter your birthday")

if birthday in pi_string:
	print("your birthday is in the pi")
	pass
else:
	print("your birthday is not in the pi")