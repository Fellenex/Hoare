#Written by Chris Keeler on July 1st, 2015

from fsm import *
from scanConstants import *
from testing import *


#Scans the text to collect an identifier
#Identifiers are comprised of solely alphabetical characters.
def collectIdentifier(text,tokens,x):
	characterStack=[]
	
	while x<len(text):
		if text[x].isalpha():
			characterStack.append(text[x])
			x+=1
		else:
			break
	
	tokens.append((sIDENTIFIER, ''.join(characterStack)))
	return x

#Scans the text to collect a number
#Numbers are of one of the following forms:
#	[0..9]*				(integer)
#	[0..9]*.[0..9]+		(decimal value)
def collectNumber(text,tokens,x):
	characterStack=[]

	while x<len(text):
		if unicode(text[x], 'utf-8').isnumeric():
			characterStack.append(text[x])
			x+=1
		else:
			print "No more numbers"
			break
	
	try:
		if text[x] == '.':
			#float number
			characterStack.append(text[x])
			x+=1
			rhs = False
			while x<len(text):
				if unicode(text[x], 'utf-8').isnumeric():
					characterStack.append(text[x])
					rhs = True
					x+=1
				else:
					break

			if rhs:
				tokens.append((sFLOAT,''.join(characterStack)))
			else:
				tokens.append((sILLEGAL, ''.join(characterStack)+text[x]))
		else:
			tokens.append((sINTEGER,''.join(characterStack)))

	except IndexError:
		#This occurs when a number is the last thing read in, because of the increment to x in the previous while loop
		tokens.append((sINTEGER,''.join(characterStack)))

	return x

#Takes some input, and creates a list of identifiers to represent what tokens exist
def scan(text):
	c=0
	tokens=[]

	while c<len(text):
		if text[c].isalpha():
			print "C is "+str(c)+" before collecting identifier"
			c = collectIdentifier(text,tokens,c)
			print "C is "+str(c)+" after collecting identifier"

		elif unicode(text[c], 'utf-8]').isnumeric():
			print "C is "+str(c)+" before collecting number"
			c = collectNumber(text,tokens,c)
			print "C is "+str(c)+" after collecting number"

		#We increment c here and below, since collectIdentifier() and collectNumber()
		#leave the counter on the next character to be scanned, but these cases do not.
		elif text[c] in outputTokens:
			print "Found a good char: "+text[c]
			tokens.append(outputTokens[text[c]])
			c+=1

		else:
			print "Found a bad char: "+text[c]
			tokens.append((sILLEGAL, text[c]))
			c+=1

	print "Finished scanning, starting writing"

	with open('scanOutput.txt','w') as f:
		for token in tokens:
			f.write(str(token)+"\n")

		f.close()

	return tokens


def runTests(answerKeyFileName,testStringsFileName):
	tests = getLines(testStringsFileName)
	answerKey = getLines(answerKeyFileName)
	testAnswers = []

	for test in tests:
		testAnswers+scan(test)
		
	score = checkAnswers(answerKey,testAnswers)
	print "Score is: "+str(len(answerKey)-score)+"/"+str(len(answerKey))


o = scan("1 12 12.34 12+34 1234")
k = scan("`~!@#$%^&*()-+=<>./")

#runTests("tests/scanner/identifiersAnswers.txt", "tests/scanner/identifiersTests.txt")