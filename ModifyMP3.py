import os
import random

# -*- coding: utf-8 -*-

print("add your path")
myPath = raw_input()

list = os.listdir(myPath)
print(list)

for i,file in enumerate(os.listdir(path)):
#	print(file)
	a = random.randint(0,999)
	b = "0"
	if (a < 100 and a > 9) :
		b = "0" + str(a)
	elif (a < 10) :
		b = "00" + str(a)
	else :
		b = str(a)
	
	newName = b + file
	print(newName)
	os.rename(os.path.join(path, file), os.path.join(path, newName))



