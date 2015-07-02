#Input tokens
inputTokens = dict()


outputTokens = dict()
outputTokens['-'] = "sNEG"
outputTokens['+'] = "sPLUS"
outputTokens['-'] = "sMINUS"
outputTokens['*'] = "sMULT"
outputTokens['/'] = "sDIV"
outputTokens['%'] = "sMOD"
outputTokens['.'] = "sDOT"
outputTokens['='] = "sEQUALS"
outputTokens['^'] = "sEXP"
outputTokens['<'] = "sLESSER"
outputTokens['>'] = "sGREATER"
outputTokens['('] = "sLPAREN"
outputTokens[')'] = "sRPAREN"

outputTokens[' '] = "sWHITESPACE"
outputTokens['\n'] = "sWHITESPACE"
outputTokens['\t'] = "sWHITESPACE"

outputTokens['@'] = "sALPHA"
outputTokens['~'] = "sNUM"
outputTokens['#'] = "sEMPTY"

sIDENTIFIER = "sIDENTIFIER"
sINTEGER = "sINTEGER"
sFLOAT = "sFLOAT"
sILLEGAL = "sILLEGAL"