file_name = "alice.txt"

try:
	with open(file_name)as fil_obj:
		contents = fil_obj.read()
	pass
except FileNotFoundError:
	print("file not found")

else:
	words = contents.split()
	num_words = len(words)
	print("The file "+file_name + " has about "+str(num_words)+" words")