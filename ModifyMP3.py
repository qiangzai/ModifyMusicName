import os
import random

# -*- coding: utf-8 -*-

print("add your path")
myPath = raw_input()

list = os.listdir(myPath)
print(list)

for i,file in enumerate(os.listdir(myPath)):
	a = random.randint(0,999)
	b = "0"
	if (a < 100 and a > 9) :
		b = "0" + str(a)
	elif (a < 10) :
		b = "00" + str(a)
	else :
		b = str(a)
	
	s = file[0:3]
	newName = ""
	print(s)
	if s.isdigit() :
		newName = file.replace(s,b)
	else :
		newName = b + file
		
	print(newName)
	os.rename(os.path.join(myPath, file), os.path.join(myPath, newName))
	
	
	
	




