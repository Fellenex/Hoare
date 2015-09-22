#Written by Chris Keeler, on June 23rd, 2015

import sys
from constants import *

#Assignment statements are one of the following forms:
#	identifier = identifier
#	identifier = expression


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

	#Step 1: Collect the subject identifier
	onceReducedAssignmentStatement,assignmentSubject = parseIdentifier(assignmentStatement)
	tokenStack.append(assignmentSubject)

	#Step 2: Validate assignment syntax
	twiceReducedAssignmentStatement = onceReducedAssignmentStatement.lstrip()
	if twiceReducedAssignmentStatement[0] != '=':
		badFormat(twiceReducedAssignmentStatement)
	else:
		tokenStack.append('=')

	#Step 3: Collect the subject expression
	thriceReducedAssignmentStatement = parseExpression(twiceReducedAssignmentStatement)

	return tokenStack


#Scans the tokens to create an identifier from a statement segment
#Identifiers are comprised of solely alphabetical characters.
#Parameters:
#	assignmentStatement: A string to be scanned and parsed for an identifier
#Return Values:
#	shiftReducedAssignmentStatement: The original assignmentStatement without the characters we just scanned through
#	identifier: The identifier found while parsing
#
def parseIdentifier(assignmentStatement):
	characterStack = []
	c=0
	while c<len(assignmentStatement):
		#append alphabetical characters onto the stack
		if assignmentStatement[c].isalpha():
			characterStack.append(assignmentStatement[c])

		#if we arrive at a non-alphabetical character, the identifier should be over
		elif assignmentStatement[c].isspace() or unicode(assignmentStatement[c], 'utf-8').isnumeric() or isIllegal(assignmentStatement[c]):
			#identifier is over now
			break

		else:
			unknownChar(assignmentStatement[c])
			break
			
		c+=1

	#Convert the list of characters into a string
	identifier = ''.join(characterStack)

	#Create a new string (to represent the remainder of the assignment statement)
	#by removing all of the bits that have been cleared off
	shiftReducedAssignmentStatement = assignmentStatement[c:len(assignmentStatement)]

	return shiftReducedAssignmentStatement, identifier

#Parameters:
#	questionableString: A string which may or mayn't be legal
#Return Value:
#	True/False, dependent on whether or not questionableString is a legal character.
#
def isLegal(questionableString):
	isInt = isFloat = False
	try:
		isInt = int(questionableString)
	except ValueError:
		isFloat = float(questionableString)
	finally:
		try:
			isFloat = float(questionableString)
		except ValueError:
			pass

	return (unicode(questionableString, 'utf-8').isnumeric() or questionableString.isalpha())


def unknownChar(spookyCharacter):
	print "Unknown character: "+spookyCharacter
	#sys.exit(80)


#Moves from the postcondition to the precondition
def collapseConditions(precondition,postcondition,statements):
	pass


def identifierGrammar():
	start = State('A')
	finish = State('B',True)

	start.addTransition(Transition(start,WHITESPACE))
	start.addTransition(Transition(finish,ALPHABETIC))
	finish.addTransition(Transition(finish,ALPHABETIC))

	idFSM = FSM()
	idFSM.addState(start)
	idFSM.addState(finish)

	#idFSM.toString()
	#for s in idFSM.states:
	#	s.getTransitions()
	return idFSM

#This FSM will consume all whitespace characters
def whitespaceGrammar():
	start = State('W',True)

	start.addTransition(Transition(start,WHITESPACE))

	wsFSM = FSM()
	wsFSM.addState(start)

	return wsFSM

def testOne():
	testStatement = "x = 5;"
	hoareDict = parseStatement(testStatement)

testOne()