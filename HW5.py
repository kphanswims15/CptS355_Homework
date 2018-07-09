# Kimi Phan
# 11466435
# Assignment 5
# Mac os/Unix

import re
#global variables
opStack = []  #assuming top of the stack is the end of the list

# modified dicStack to have a default value
dictStack = [(0,{})]  #assuming top of the stack is the end of the list

# global varible that tells which scoping rules you want to use
scopingDynamic = True

#------- Operand Stack Operators --------------
#Pop a value from opStack.
def opPop():
    if len(opStack) > 0:
        x = opStack[len(opStack) - 1]
        opStack.pop(len(opStack) - 1)
        return x
    else:
        print("Error: opPop - Operand stack is empty")

#the Postscript pop; doesn't return the popped value
def pop():  
    if len(opStack) > 0:
        x = opStack[len(opStack) - 1]
        opStack.pop(len(opStack) - 1)
    else:
        print("Error: pop - Operand stack is empty")

#Push a value to opStack.
def opPush(value):
    opStack.append(value)
    
#Pop a value from dictStack.
def dictPop():
    if len(dictStack) > 0: 
        dictStack.pop(len(dictStack) - 1)
    else:
        print("Error: Pop - Operand stack is empty")

#------- Dict Stack Operators --------------
#pop the empty dictionary off the operand stack and push it on the dictStack
# modified to support tuples
def dictPush(func, d):
    linkVal = 0
    if scopingDynamic == True:
        # find the link value for dynamic scoping
        if len(dictStack) != 0:
            linkVal = len(dictStack) - 1
    else:
        # find the link value for static scoping
        i = len(dictStack) - 1

        while (i > 0):
            # searches the dictionary for the function
            if ("/" + func) in dictStack[i][1]:
                linkVal = i
                break
            else:
                # terminates the while loop
                i = dictStack[i][0]

    if isinstance(d,dict):
        # appends a tuple to the dictStack with the link value and a dictionary
        dictStack.append((linkVal, d))
    else:
        opPush(d)
        print("Error : DictPush - Expecting a dictionary on the top of the operand stack")

#add a variable definition to the top of the stack. Adds a new dictionary if the stack is empty.
# modfied to support tuples in the dictStack
def define(name, value):

    linkVal = len(dictStack) - 1

    # checks if it is the dictionary then updates the value
    if len(dictStack) > 0:
        dictStack[-1][1][name] = value
    else:
        newDict = {}
        newDict[name]= value
        # if not in a dictionary then append the linkvalue and an empty dictionary
        dictStack.append((linkVal, newDict))
        #opPush(newDict)
        #dictPush()

#search the dictStack for a variable or function (start searhing at the top of the stack)
# modified to support tuples in the dictStack
def lookup(name):

    i = len(dictStack) - 1
    while (i > 0):
        if (dictStack[i][1].get("/" + name, 0)): ##append '/' to name
            return dictStack[i][1]["/" + name]
        else:
            i = dictStack[i][0]

    if dictStack[i][1].get("/"+ name, 0):
        return dictStack[i][1]["/" + name]
    else:
        return None

#------- Arithmetic Operators --------------
##pop 2 values from stack; check if they are numerical (int or float); add them; push the result back to stack. 
def add():
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if((isinstance(op1,int) or isinstance(op1, float))
           and (isinstance(op2,int) or isinstance(op2,float))):
            opPush(op1+op2)
        else:
            print("Error: add - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: add expects 2 operands")

##pop 2 values from stack; check if they are numerical (int or float); subtract them; push the result back to stack. 
def sub():
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if((isinstance(op1,int) or isinstance(op1, float))
           and (isinstance(op2,int) or isinstance(op2,float))):
            opPush(op2-op1)
        else:
            print("Error: sub - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: sub expects 2 operands")

##pop 2 values from stack; check if they are numerical (int or float); multiply them; push the result back to stack. 
def mul():
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if((isinstance(op1,int) or isinstance(op1, float))
           and (isinstance(op2,int) or isinstance(op2,float))):
            opPush(op1*op2)
        else:
            print("Error: mul - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: mul expects 2 operands")

##pop 2 values from stack; check if they are numerical (int or float); divide the top value with the other; push the result back to stack. 
def div():
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if((isinstance(op1,int) or isinstance(op1, float))
           and (isinstance(op2,int) or isinstance(op2,float))):
            opPush(op2/op1)
        else:
            print("Error: div - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: div expects 2 operands")
            
##pop 2 values from stack; check if they are numerical (int or float); calculate the mod; push the result back to stack.         
def mod():
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if((isinstance(op1,int) or isinstance(op1, float))
           and (isinstance(op2,int) or isinstance(op2,float))):
            opPush(op2 % op1)
        else:
            print("Error: div - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: div expects 2 operands")


#------- Array Operators --------------
#Pops an array value from the operand stack and calculates the length of it. Pushes the length back to the stack.
def length():
    if len(opStack) > 0:
        aInput = opPop()
        if(isinstance(aInput, list)):
            opPush(len(aInput))
        else:
           print("Error: length expects an array/list argument")
           opPush(aInput)
    else:
        print("Error: length - not enough arguments")
        
#Pops a array value and an index from the operand stack and pushes the value at the index position of the array onto the opStack
def get():
    if len(opStack) > 1:
        ind = opPop()
        aInput = opPop()
        if(isinstance(aInput,list) and isinstance(ind, int)):
            opPush(aInput[ind])
        else:
            print("Error: get expects a string and an integer argument")
            opPush(aInput)
            opPush(ind)
    else:
        print("Error: get - not enough arguments")

def forall():
    if len(opStack) > 1:
        fbody = opPop()
        aInput = opPop()
        if (isinstance(aInput, list) and isinstance(fbody, list)):
            for x in aInput:
                opPush(x)  # push the array element onto the stack
                interpretSPS(fbody)
        else:
            print("Error: forall expects an array and a codearray")
            opPush(aInput)
            opPush(fbody)
    else:
        print("Error: get - not enough arguments")




#------- Stack Manipulation and Print Operators --------------

#copies top element in opStack
def dup():
    if len(opStack) > 0:
        op1 = opPop()
        opPush(op1)
        opPush(op1)
    else:
        print("Error: dup - not enough arguments")

#pops an integer count from stack, copies count characters and pushes them back to stack. 
def copy():
    if(len(opStack) > 0):
        count = opPop()
        copyList = []
        for  x in range(0,count):
            copyList.append(opPop())
        for item in reversed(copyList):
            opPush(item)
        for item in reversed(copyList):
            opPush(item)
    else:
        print("Error: copy - not enough arguments")

#pops the top value from the operand stack
def pop ():
    if (len(opStack) > 0):
        opPop()
    else:
        print("Error: copy - not enough arguments")

#clears the stack
def clear():
    del opStack[:]
    del dictStack[:]
    dictStack.append((0,{}))
    
#prints the stack
# modified to print the dictionary stack along with the links and indexes
def stack():
    if scopingDynamic == True:
        print("Dynamic")
    else:
        print("Static")

    print("===========")
    for i in reversed(opStack):
        print(i)
    print("===========")
    for i in reversed(dictStack):
        print("---{}---{}---".format(dictStack.index(i), i[0]))
        for k, v in i[1].items():
            print(k, v)
    print("===========")

#swaps the top two elements in opStack
def exch():
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        print("Error: exch - not enough arguments")

#Pops 2 integer values m and n from stack, rolls the top m values n times (if n is positive roll clockwise, otherwise roll countercloackwise)
def roll():
    if len(opStack) > 1:
        n = opPop()
        m = opPop()
        copyList = []
        for x in range(0,m):
            copyList.append(opPop())
        if (n>0): 
            copyList[len(copyList):] = copyList[0:n]
            copyList[0:n]=[]
        else:
            copyList[:0]=copyList[n:]
            copyList[n:]=[]
       
        for x in reversed(copyList[0:]):
            opPush(x)
        del copyList[:]
          
    else:
       print("Error: roll - not enough arguments")



#creates a new empty dictionary  pushes it on the opStack
#def psDict():
 #   if len(opStack) > 0:
  #      n = opPop() # n is the initial size of the dictionary ; discard
   #     opPush({})
   # else:
    #    print("Error: psDict - not enough arguments")

#def begin():
 #   dictPush(opPop())

#def end():
 #   dictPop()
    
#pops a name and a value from stack, adds the definition to the dictStack. 
def psDef():
    if len(opStack) > 1:
        value = opPop()
        name = opPop()
        if(isinstance(name,str)):
            define(name, value)
        else:
            print("Error: psDef - invalid name argument")
    else:
        print("Error: psDef - not enough arguments")
        
#------- Loop Operators --------------

#for loop
def For():
    forBody = opPop()
    end = opPop()
    inc = opPop()
    begin = opPop()

    for x in range(begin,end,inc):
        opPush(x) #push the loop index onto stack at each iteration
        interpretSPSS(forBody)
        
    
#------- Parsing Functions --------------        

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def tokenize(s):
    retValue = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    return retValue

def groupMatching(it):
    res = []
    for c in it:
        if c=='}':
            return res
        elif c=='{':
            res.append(groupMatching(it))
        else:
            if isInt(c):
                res.append(int(c))
            else:
                res.append(c)
    return False


def parse(s):
    res = []
    it = iter(s)
    for c in it:
        if c=='}':  #non matching closing paranthesis
            return False
        elif  c=='{':
            res.append(groupMatching(it))
        else:
            if isInt(c):  
                res.append(int(c))
            elif isinstance(c, str):
                if c[0] == '[':     #token is an array constant ; remove () before pushing onto the stack
                    aList = c[1:-1].split(' ')
                    res.append([int(x) for x in aList])
                else:
                    res.append(c)
            else:
                res.append(c)
    return res

#the main recursive interpreter function
# modified to support scoping rules
def interpretSPSS(tokenList):
    #this dictionary holds all functions the user can call
    builtinFunctions = {
        "add":add,
        "sub":sub,
        "mul":mul,
        "div":div,
        "mod":mod,
        "length":length,
        "get":get,
        "dup":dup,
        "exch":exch,
        "pop":pop,
        "roll":roll,
        "copy":copy,
        "clear":clear,
        "stack":stack,
        #"dict":psDict,
        #"begin":begin,
        #"end":end,
        "def":psDef,
        "for":For,
        "forall":forall}

    for token in tokenList:
        if isinstance(token, int): #token is an integer constant
            opPush(token)
        elif isinstance(token, str):
            if token[0] == '/' :  #token is a name
                opPush(token)
            else:
                func = builtinFunctions.get(token,None)  #token is a built-in function
                if func != None:
                    func()
                else:       # token is not a fucntion, should be a variable lookup.
                    val = lookup(token)
                    if isinstance(val,list):   #check if val is a code array, if so interpret the code array body.
                        dictPush(token, {}) # pushes a dictionary once a function is called
                        interpretSPSS(val)
                        dictPop() # pops off the top dictionary after the function is excuted
                    elif val != None:           # the returned value is not a code array, should be a variable value; push it on the operand stack
                        opPush(val)
                    else:       #neither variable or function; couldn't find a value in dictStack. Give an error!
                        print("Error: Couldn't find " + token + "in the dictStack!")
        elif isinstance(token, list): #code array or constant array
            opPush(token)
        else:      #if none of the above give an error.
            print("Error: Undefined token  in input!")


#parses the input string and calls the recursive interpreter to solve the
#program
# modified to support different scoping rules
def interpreter(s, scope):
    tokenL = parse(tokenize(s))

    global scopingDynamic
    if scope == "dynamic":
        scopingDynamic = True
    else:
        scopingDynamic = False

    interpretSPSS(tokenL)



def main_partB():
#---------Test Case 1 -------
    testcase1= """
    /fact{
       /n exch def
       1
    n -1 1 {mul} for
    }def
    [1 2 3 4 5] dup 4 get pop
    length
    fact
    stack
    """
    interpreter(testcase1, "dynamic")
    clear()
    interpreter(testcase1, "static")
    #output should print [120]
    clear() #clear the stack for next test case

#---------Test Case 2 -------
    testcase2 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """
    interpreter(testcase2, "dynamic")
    clear()
    interpreter(testcase2, "static")
    #output should print [7]
    clear() #clear the stack for next test case

#---------Test Case 3 -------
    testcase3 = """
     /m [25 50] 1 get  def
     /n [100 1] 0 get  def
     /egg1 {/m 25 def n} def
     /chic {
     /n 1 def
     /egg2 { n } def
     m  n
     egg1
     egg2
     stack  } def
     n
     chic
    """
    interpreter(testcase3, "dynamic")
    clear()
    interpreter(testcase3, "static")
    #output should be
    #[100,50,1,1,1]
    clear() #clear the stack for next test case

if __name__ == '__main__':
    print(main_partB())


