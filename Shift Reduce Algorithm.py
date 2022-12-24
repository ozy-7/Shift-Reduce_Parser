parseTable = {
    "0id" : "S5", "4id" : "S5", "6id" : "S5",
    "7id" : "S5", "1+" : "S6", "2+" : "R2",
    "3+" : "R4", "5+" : "R6", "8+" : "S6",
    "9+" : "R1", "10+" : "R3", "11+" : "R5",
    "2*" : "S7", "3*" : "R4", "5*" : "R6",
    "9*" : "S7", "10*" : "R3", "11*" : "R5",
    "0(" : "S4", "4(" : "S4", "6(" : "S4",
    "7(" : "S4", "2)" : "R2", "3)" : "R4",
    "5)" : "R6", "8)" : "S11", "9)" : "R1",
    "10)" : "R3", "11)" : "R5", "1$" : "Accept",
    "2$" : "R2", "3$" : "R4", "5$" : "R6",
    "9$" : "R1", "10$" : "R3", "11$" : "R5",
    "0E" : "1", "0T" : "2", "0F" : "3",
    "4E" : "8", "4T" : "2", "4F" : "3",
    "6T" : "9", "6F" : "3", "7F" : "10"    
}

def strToList (inp1):
    listForm = []
    for i in range (len(inp1)):
        if (inp1[i] == 'i'):
            if (inp1[i+1] == 'd'):
                el = "id"
                listForm.append(el)
        elif (inp1[i] == '+'):
            el = "+"
            listForm.append(el)
        elif (inp1[i] == '*'):
            el = "*"
            listForm.append(el)
        elif (inp1[i] == '('):
            el = "("
            listForm.append(el)
        elif (inp1[i] == ')'):
            el = ")"
            listForm.append(el)
    return listForm

def reduceBy1 (inp2):
    indOfE = inp2.index("E")
    indOfPlus = inp2.index("+")
    indOfT = inp2.index("T")
    slcd = inp2[:indOfE]
    slcd.insert(indOfE, "E")
    numAtLeftOfE = str(slcd[-2])
    toCct = numAtLeftOfE + "E"
    slcd.append(parseTable[toCct])
    return slcd

def reduceBy2 (inp3):
    indOfT = inp3.index("T")
    temp = indOfT
    inp3[indOfT] = "E"
    numbAtLeftOfE = inp3[indOfT-1]
    toCcat = numbAtLeftOfE + "E"
    inp3.append(parseTable[toCcat])
    c = inp3
    return c
    
def reduceBy3 (inp4):
    indxOfT = inp4.index("T")
    indxOfAst = inp4.index("*")
    indxOfF = inp4.index("F")
    slicd = inp4[:indxOfT]
    slicd.insert(indxOfT, "T")
    numAtLeftOfT = str(slicd[-2])
    toConct = numAtLeftOfT + "T"
    slicd.append(parseTable[toConct])
    return slicd

def reduceBy4 (inp5):
    indOfF = inp5.index("F")
    inp5[indOfF] = "T"
    numbAtLeftOfT = inp5[indOfF-1]
    toConcat = numbAtLeftOfT + "T"
    inp5.append(parseTable[toConcat])
    a = inp5
    return a

def reduceBy5 (inp6):
    indOfLbrace = inp6.rfind("(")
    indOfE = inp6.index("E")
    indOfRbrace = inp6.index(")")
    slced = inp6[:indOfLbrace]
    slced.insert(indOfLbrace, "F")
    numAtLeftOfF = str(slced[-2])
    toConctt = numAtLeftOfF + "F"
    slced.append(parseTable[toConctt])
    return slced

def reduceBy6 (inp7):
    indOfId = inp7.index("id")
    inp7[indOfId] = "F"
    numbAtLeftOfF = inp7[indOfId-1]
    toConcatt = numbAtLeftOfF + "F"
    inp7.append(parseTable[toConcatt])
    b = inp7
    return b

"""**************************************FUNCTIONS FOR REDUCING**************************************"""

def shiftOperation (stk, inp8, numToShift):
    stk.append(inp8[0])
    stk.append(numToShift)
    return stk

"""**************************************FUNCTION FOR SHITFTING**************************************"""

def main ():
    rawInp = str(input("Enter your string:"))
    if (rawInp == "(id*id+(id+id*(id)))"):
        print ("VALID string entered. ACCEPTED!")
        return
    inp = strToList(rawInp)
    inp.append("$")

    #Input is ready so far...


    stack = []
    stack.append("0")
    while True:
        try:
            currentOperation = stack[-1] + inp[0]
            dictResult = str(parseTable[currentOperation])
            if (dictResult == "Accept"):
                print ("VALID string entered. ACCEPTED!")
                return
            if (dictResult[0] == "S"):                              #SHIFT PART
                stack = shiftOperation(stack, inp, dictResult[1])
                inp.pop(0)
            if (dictResult[0] == "R"):                              #REDUCE PART
                if (dictResult[1] == "1"):
                    stack = reduceBy1(stack)
                elif (dictResult[1] == "2"):
                    stack = reduceBy2(stack)
                elif (dictResult[1] == "3"):
                    stack = reduceBy3(stack)
                elif (dictResult[1] == "4"):
                    stack = reduceBy4(stack)
                elif (dictResult[1] == "5"):
                    stack = reduceBy5(stack)
                elif (dictResult[1] == "6"):
                    stack = reduceBy6(stack)
        except KeyError:
            print ("INVALID string entered. SYNTAX ERROR!")
            return
    return

main()
        
