# -*- coding: utf-8 -*-

def rbfk(n):
	"""
	Create the constraints of RBFK
	1 byte Variables
	 X = (x0, x1, ---, x7)
	MSB = X0, LSB = X7
	"""	
	model = "rbfk.lp"
	fileobj = open(model, "a")
	
	for i in range(4):
		if i<2:
			fileobj.write("x_" + str(n) + "_" + str(i) + " - x_" + str(n+1) + "_" + str(i+2) + " = 0")
			fileobj.write("\n")	
		else:
			fileobj.write("x_" + str(n) + "_" + str(i+4) + " - x_" + str(n+1) + "_" + str(i+2) + " = 0")
			fileobj.write("\n")	

	# xor with G_L
	fileobj.write("x_" + str(n) + "_1 + x_" + str(n) + "_4 + x_" + str(n+1) + "_0 - 2 d_" + str(n) + "_0 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_0 - x_" + str(n) + "_1 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_0 - x_" + str(n) + "_4 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_0 - x_" + str(n+1) + "_0 >= 0")
	fileobj.write("\n")
	
	fileobj.write("x_" + str(n) + "_0 + x_" + str(n) + "_5 + x_" + str(n+1) + "_1 - 2 d_" + str(n) + "_1 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_1 - x_" + str(n) + "_0 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_1 - x_" + str(n) + "_5 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_1 - x_" + str(n+1) + "_1 >= 0")
	fileobj.write("\n")
	
	# xor with G_R
	fileobj.write("x_" + str(n) + "_2 + x_" + str(n) + "_7 + x_" + str(n+1) + "_6 - 2 d_" + str(n) + "_2 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_2 - x_" + str(n) + "_2 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_2 - x_" + str(n) + "_7 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_2 - x_" + str(n+1) + "_6 >= 0")
	fileobj.write("\n")
			
	fileobj.write("x_" + str(n) + "_3 + x_" + str(n) + "_6 + x_" + str(n+1) + "_7 - 2 d_" + str(n) + "_3 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_3 - x_" + str(n) + "_3 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_3 - x_" + str(n) + "_6 >= 0")
	fileobj.write("\n")
	fileobj.write("d_" + str(n) + "_3 - x_" + str(n+1) + "_7 >= 0")
	fileobj.write("\n")

	# Active-Sbox
	for i in range(4):
		if i<2:
			fileobj.write("A_" + str(n) + "_" + str(i) + " - x_" + str(n) + "_" + str((i)) + " >= 0")
			fileobj.write("\n")
		else:
			fileobj.write("A_" + str(n) + "_" + str(i) + " - x_" + str(n) + "_" + str((i+4)) + " >= 0")
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