# -*- coding: utf-8 -*-

from Rbfk_LCP_functions import *

model = "rbfk.lp"
fileobj = open(model, "w")

# target round
R = 50

"""
Create object function
"""	
fileobj.write("Minimize")
fileobj.write("\n")

for n in range(1,R+1):
	for i in range(4):
		if(n==R) & (i==3):
			fileobj.write("A_"+ str(n) + "_" + str(i))
		else:
			fileobj.write("A_"+ str(n) + "_" + str(i) + " + ")

fileobj.write("\n")

"""
Create the constraints of RBFK
"""	
fileobj.write("Subject To")
fileobj.write("\n")
fileobj.close()

for n in range(1, R+1):
	rbfk(n)

"""
Input Differential characteristic
"""	
model = "rbfk.lp"
fileobj = open(model, "a")

for i in range(8):
	if i==7:
		fileobj.write("x_"+ str(R+1) + "_" + str(i) + " >= 1")
		fileobj.write("\n")
	else:
		fileobj.write("x_"+ str(R+1) + "_" + str(i) + " + ")
			
fileobj.write("Binary")
fileobj.write("\n")
fileobj.close()

# 1st,...,rth round variables
for i in range(1, R+1):
	Variables(i)
	
model = "rbfk.lp"
fileobj = open(model, "a")
fileobj.write("END")
fileobj.write("\n")
fileobj.close()