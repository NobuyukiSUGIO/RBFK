# -*- coding: utf-8 -*-

def rbfk(n):
	"""
	Create the constraints of RBFK
	1 byte Variables
	X^r = (x_r_0, x_r_1, ---, x_r_7)
	r : round
	MSB = X_r_0, LSB = X_r_7
	"""	
	model = "rbfk.lp"
	fileobj = open(model, "a")
	
	# xor 
	for i in range(4):
		if i<2:
			fileobj.write("x_" + str(n) + "_" + str(i+4) + " - x_" + str(n+1) + "_" + str(i) + " = 0")
			fileobj.write("\n")	
		else:
			fileobj.write("x_" + str(n) + "_" + str(i) + " - x_" + str(n+1) + "_" + str(i+4) + " = 0")
			fileobj.write("\n")	

	# copy with G_L
	fileobj.write("x_" + str(n) + "_0 + x_" + str(n+1) + "_1 + x_" + str(n+1) + "_2 - 2 d_" + str(n) + "_0 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_0 - x_" + str(n) + "_0 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_0 - x_" + str(n+1) + "_1 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_0 - x_" + str(n+1) + "_2 >= 0")
	fileobj.write("\n")
	
	fileobj.write("x_" + str(n) + "_1 + x_" + str(n+1) + "_0 + x_" + str(n+1) + "_3 - 2 d_" + str(n) + "_1 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_1 - x_" + str(n) + "_1 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_1 - x_" + str(n+1) + "_0 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_1 - x_" + str(n+1) + "_3 >= 0")
	fileobj.write("\n")
	
	# copy with G_R
	fileobj.write("x_" + str(n) + "_6 + x_" + str(n+1) + "_4 + x_" + str(n+1) + "_7 - 2 d_" + str(n) + "_2 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_2 - x_" + str(n) + "_6 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_2 - x_" + str(n+1) + "_4 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_2 - x_" + str(n+1) + "_7 >= 0")
	fileobj.write("\n")
			
	fileobj.write("x_" + str(n) + "_7 + x_" + str(n+1) + "_5 + x_" + str(n+1) + "_6 - 2 d_" + str(n) + "_3 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_3 - x_" + str(n) + "_7 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_3 - x_" + str(n+1) + "_5 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_3 - x_" + str(n+1) + "_6 >= 0")
	fileobj.write("\n")

	# Active-Sbox
	for i in range(4):
		if i<2:
			fileobj.write("A_" + str(n) + "_" + str(i) + " - x_" + str(n+1) + "_" + str((i)) + " >= 0")
			fileobj.write("\n")
		else:
			fileobj.write("A_" + str(n) + "_" + str(i) + " - x_" + str(n+1) + "_" + str((i+4)) + " >= 0")
			fileobj.write("\n")
	
	fileobj.close()
	
def Variables(n):
	"""
	Generate variables.
	"""	
	model = "rbfk.lp"
	fileobj = open(model, "a")
	
	variable = []
	
	"""
	Generate variables for slim.
	"""
	# 1st - nth round variables
	for i in range(8):
		fileobj.write("x_" + str(n) + "_" + str(i))
		fileobj.write("\n")
	for i in range(4):
		fileobj.write("d_" + str(n) + "_" + str(i))
		fileobj.write("\n")
	for i in range(4):
		fileobj.write("A_" + str(n) + "_" + str(i))
		fileobj.write("\n")

	for i in range(len(variable)):
		var = variable[i]
		fileobj.write(str(var)) 
		fileobj.write("\n")
	fileobj.close()
	return variable