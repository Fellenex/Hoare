#An expression is built using the following CFG:
#
# E --> (E) | R
# R --> E * R | E / R | S
# S --> E + S | E - S | T
# T --> E | identifier | numeric

import fsm
import constants
import parse

# E --> identifier | numeric | Q | (E)
# Q --> R | E ^ R
# R --> S | E * R | E / R
# S --> T | E + S | E - S

def expressionGrammar():

	start = State(EXPRESSION)
	exponents = State(EXPONENTS)
	multidiv = State(MULTIDIV)
	addsub = State(ADDSUB)
	atoms = State(ATOMS)


	start.addTransition(PDA_Transition(exponents,EMPTY,EMPTY,EMPTY))
	start.addTransition(PDA_Transition(start,LPAREN,LPAREN,EMPTY))

	exponents.addTransition(PDA_Transition(multidiv,EMPTY,EMPTY,EMPTY))

	multidiv.addTransition(PDA_Transition(addsub,))


	atom.addTransition(PDA_Transition())

	#We use # to represent the empty string.
	start.addTransition(PDA_Transition(start,EMPTY,'(',''))
	start.addTransition(PDA_Transition(exponents,))


def E(stack,expString):
	handleList = [EXPONENTS, '('+EXPRESSION+')']

def Q(stack,expString):
	handleList = [MULTIDIV, EXPRESSION+'^'+]

def R(stack,expString):
	pass

def S(stack,expString):
	pass

def T(stack,expString):
	#Any number of alphabetics or numerics lump themselves into an identifier
	handleList = [ALPHABETIC,NUMERIC,EXPRESSION]








#Parses an expression
#Precedence is as follows:
#	unary -
#	*, /
#	+, -
#
def parseExpression(expString):
	collectionStack = []

	idFSM = identifierGrammar()
	wsFSM = whitespaceGrammar()
	exFSM = expressionGrammar()

	c=0
	while c<len(expString):




	c = 0
	while c<len(expString):
		#If we have run into an alphabetical character, then this should be the start of an identifier
		if assignmentStatement.isalpha():
			parseIdentifier


	for i in range(len(expString)):
		parseStack.append(expString[i])
	
	while len(parseStack)>0:
		pass #todo parse here