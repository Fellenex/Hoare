#Assignment statements are one of the following forms:
#	identifier = identifier
#	identifier = expression

#An expression is built using the following CFG:
#
# E --> ( E ) | R
# R --> E * R | E / R | S
# S --> E + S | E - S | T
# T --> E | identifier | numeric
#

class Environment():
	def __init__(self):
		self.variables = dict()

	def setVariable(self,varName,varValue):
		self.variables[varName] = varValue


class HoareStatement():
	def __init__(self,_LHS,_RHS):
		self.LHS = _LHS
		self.RHS = _RHS

	def toString(self):
		print self.LHS, '=', self.RHS



#Scans and parses one assignment statement
#Generates a dictionary to be used for the creation of a new Hoare statement
def parseStatement(assignmentStatement):
	assignmentSubject = ""
	tokenStack = []
	c=0
	while c<len(assignmentStatement):
		if assignmentStatement[c] == '=':



		c++ #hehe

	newHoareStatement = "true"
	return newHoareStatement

#Parses an expression
def isExpression(expString):
	parseStack = []
	tokenStack = []

	for i in range(len(expString)):
		parseStack.append(expString[i])
	
	while len(parseStack)>0:
		pass #todo parse here

#Moves from the postcondition to the precondition
def collapseConditions(precondition,postcondition,statements):
