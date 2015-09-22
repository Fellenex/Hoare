from fsm import *

#start with {q0}
#add all transitions to the stack
#all transition state sets get added as new states

#_stateSet is a State object, which often is composed of a subset of the states duped into one
#_alphabet is a list of characters
def generateStateSet(_stateSet, _alphabet):
	newTransitions = dict()
	for c in _alphabet:
		newTransitions[c] = []

	#Look 
	for state in _stateSet:
		for transition in state.transitions:
			newTransitions[transition.label].append(transition)

	return newTransitions


def convertNFA(_nfa):
	if _nfa.deterministic:
		return _nfa

	equivalentDFA = FSM()
	newStates = []

	#If there are multiple starting states, then add them all to the queue.
	if isinstance(_nfa.startState, list):
		memoizedStates = _nfa.startState[:]
		stateQueue = _nfa.startState[:]
	else:
		memoizedStates = [_nfa.startState]
		stateQueue = []
		stateQueue.append([_nfa.startState])

	while len(stateQueue) > 0:
		activeStateSet = stateQueue.pop(0)

		if len(activeStateSet) == 1:
			#We are only looking at one state this time. Starting out, or determinism is afoot!

			if activeStateSet[0].deterministic:
				#Then we don't need to bother trying to convert anything!
				#This is a necessary state, to be kept as is.
				newStates.append(activeStateSet[0])

				#We must however add the states reachable from this state to the stateQueue and memoized states
				#We get all of the destination states of the transitions of the state, and then filter out the ones already memoized, to prevent recomputing them.
				#Create a list of all of the 
				stateSets = filter(lambda y : y not in memoizedStates, map(lambda x: x.transitions.destination, activeStateSet[0]))
			
			else:
				#Then we need to figure out what other state sets must be merged/generated
				newTransitions = dict()
				for c in _nfa.alphabet:

					#Create a list of all of the states which are reachable from a transition using this letter of the FSM's alphabet
					newTransitions[c] = map(lambda y : y.destination, filter(lambda x : x.label == c, activeStateSet[0].transitions))

					#Continue from here



				#Look through every transition, and create sets of states
				for transition in activeStateSet[0].transitions:
					newTransitions[transition.label].append(transition.destination)

				for newTransition in newTransitions:
					if len(newTransition) == 0:
						#no transition with this character
						pass
					elif len(newTransition) == 1:
						#one transition with this character


		elif len(activeStateSet) > 1:
			#We are looking at a subset of states this time.

			for state in stateQueue[0]:
				pass
		else:
			#Something's gone wrong!
			print "Oopsy daisy"

		newTransitions = dict()
		for c in _nfa.alphabet:
			newTransitions[c] = []