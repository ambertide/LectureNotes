from os import listdir

files = listdir(".")
for file_ in files:
	if file_.endswith(".c"):
		print(file_)
		with open(file_, "r") as file_read:
			data = file_read.read()
		with open(file_ + "verbatim", "w") as file_write:
			data = data.replace("\t", "  ")
			file_write.write(data)

