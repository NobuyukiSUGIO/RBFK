# -*- coding: utf-8 -*-

from gurobipy import *

class Rbfk:
	def __init__(self):
		self.filename_result = "result.txt"
		
	def SolveModel(self):
		m = read("rbfk.lp")
		m.optimize()
		print(m.Status)
		m.printAttr('x')
		m.write("result.sol")