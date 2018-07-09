# Kimi Phan
# Student ID: 11466435
# Homework 2 Part B
# Mac OS/Unix

# For tokenizing pack for regular expressions
import re

# debugging function that can be turned on and off by changing a single variable
debugging = True
def debug(*s):
    if debugging:
        print(*s)

# The Operand Stack

# The operand stack: define the operand stack and its operations
opstack = []

# pop values off the opstack
def opPop():
    if not opstack:
        print("The stack is empty.")
    else:
        # this will pop off the last element in the list
        x = opstack.pop()
        # return the popped value
        return x

# pushing values onto the opstack
def opPush(value):
    # checks the type of value
    if isinstance(value, int) or isinstance(value, float) or isinstance(value, list) or isinstance(value, dict) or isinstance(value, str):
        if isinstance(value, str) and value[0] == '/':
            value = value[1:]
        # this will push values at the end of the stack if it is a right type
        opstack.append(value)
    else:
        print('It is not that right type')


# 2. The Dictionary Stack

# The dictionary stack: define the dictionary stack and its operations
dictstack = []

# pops the top dictionary from the dictionary stack
def dictPop():
    # pops the last dictionary from the end of the list
    x = dictstack.pop()
    # returns the dictionary
    return x

# pushes a new dictionary to the dicstack
def dictPush(d):
    # checks if the value is a dictionary
    if isinstance(d, dict):
        # pushes a new dictionary to the end of the list if it is the same type
        dictstack.append(d)
    else:
        print('It is not the right type')

# adds name:value to the top dictionary in the dictionary stack
def define(name, value):
    d = {}
    # checks if dictack is empty
    if not dictstack:
        # pushes an empty dictionary onto dict stack
        dictPush(d)
    # pops the top dictionary in the list to get access to the dictionary
    d = dictPop()
    # adds a value in the dictionary or modifies it
    d[name] = value
    # pushes the popped dictionary back into the stack
    dictPush(d)

# 3. Operators

# adds the top two numbers on the opstack
def add():
    op1 = opPop() # operand 1
    op2 = opPop() # operand 2
    # checks if the numbers are the right types
    if (isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float)):
        # pushes the sum onto the opstack
        opPush(op2 + op1)
    else:
        print('It is not that right type')

# subtracts the top two numbers on the opstack
def sub():
    op1 = opPop() # operand 1
    op2 = opPop() # operand 2
    # checks if the numbers are the right types
    if (isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float)):
        # pushes the difference on the opstack
        opPush(op2 - op1)
    else:
        print('It is not that right type')

# multiplies the top two numbers on the opstack
def mul():
    op1 = opPop() # operand 1
    op2 = opPop() # operand 2
    # checks if the numbers are the right types
    if (isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float)):
        # pushes the product on the opstack
        opPush(op2 * op1)
    else:
        print('It is not that right type')

# divides the top two numbers on the opstack
def div():
    op1 = opPop() # operand 1
    op2 = opPop() # operand 2
    # checks if the numbers are the right types
    if (isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float)):
        # pushes the quotient on the opstack
        opPush(op2 / op1)
    else:
        print('It is not that right type')

# mods the top two numbers on the opstack
def mod():
    op1 = opPop() # operand 1
    op2 = opPop() # operand 2
    # checks if the numbers are the right types
    if (isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float)):
        # pushes the remainder on the opstack
        opPush(op2 % op1)
    else:
        print('It is not that right type')

# finds the length of a list from the opstack
def length():
    op1 = opPop() # pops the last element in the opstack
    # checks if the value that is popped is a list
    if isinstance(op1, list):
        # finds the length of the list and pushes the length onto the opstack
        opPush(len(op1))
    else:
        print('It is not the right type')

# gets a value from a list that are popped from the opstack
def get():
    op1 = opPop() # index
    op2 = opPop() # a list
    try:
        opPush(op2[op1])
    except:
        print("It does not work")
        exit()

# stack manipulation

# duplicates the top element
def dup():
    # pops off the top element on the stack
    op1 = opPop()
    # pushed the element twice on the stack to duplicate it
    opPush(op1)
    opPush(op1)

# swtiches the top to elements
def exch():
    op1 = opPop() # pops off the fist element on the stack
    op2 = opPop() # pops off the second element on the stack
    opPush(op1) # pushes the fist element on the stack
    opPush(op2) # pushes the second element on the stack

# pops the top value on the stack
def pop():
    op1 = opPop()
    return op1

# move the top n values on the stack into the m th stack position
def roll():
    li = []
    op1 = opPop() # position where you want to move the elements
    op2 = opPop() # number of values you want to move
    # checks if op1 and op2 are the right type
    if isinstance(op1, int) and isinstance(op2, int):
        # rolls the elements from the top
        if op1 >= 0:
            # make sure you are rolling more than 1 element
            if op2 > 1:
                # goes through the opstack how ever many times the value of op2 is
                for i in range(op1):
                    # pops elements off of the opstack
                    op3 = opPop()
                    # pushes them into a seperate list
                    li.append(op3)
                # reverse the list because it append pushes onto the end of the list
                li.reverse()
                # puts the list into the opstack
                opstack[(-(op1- op2)) : (-(op1 - op2) - 1)] = li
            else:
                print('Not enough elements to roll')
        # move the last n of the top m values  to the top of the stack
        else:
            # make sure you are rolling more than 1 element
            if op2 > 1:
                op1 = -op1
                # goes through the opstack how ever many times the value of op2 is
                for i in range(op1):
                    # pops the values at the nth element
                    op3 = opstack.pop(-op2)
                    # pushes it to the top of the stack
                    opPush(op3)
            else:
                print('Not enough elements to roll')
    else:
        print('It is not that right type')

# copy the n stack values onto the stack
def copy():
    op1 = opPop() # number of elements to copy
    list = opstack[-op1:] # puts the copied elements in the list
    # pushes the elements onto the list in stack style
    for i in list:
        opPush(i)

# clears the stacks
def clear():
    opstack.clear()
    dictstack.clear()

# prints the stack
def stack():
    for x in reversed(opstack):
        print(x)

# dictionary operators

# pushes and empty dictionary onto the dict list
def psDict():
    op1 = opPop()
    d = {}
    opPush(d)

# takes a dictionary from the top of the operand stack and pushes it on the
# the dictionary stack
def begin():
    d = opPop() # pops off the first dictionary in the opstack
    # checks if d is the right type
    if isinstance(d, dict):
        # pushes it on dicStack if the type is right
        dictPush(d)
    else:
        print('It is not that right type')

# pops off the top dictionary and throws it away
def end():
    op1 = dictPop()

# creates or modifies a dictionary entry in the top most dictionary stack
def psDef():
    op1 = opPop() # pops off the value
    op2 = opPop() # pops off the name

    if isinstance(op2, str):
        define(op2, op1)
    else:
        print('It is not that right type')

# searches the dictionaries on the dictionary stack starting at the top to find one that
# contains name
def lookup(name):
    for i in dictstack:
        if name in i:
            value = i.get(name)
            return value
    return name

# test function for define
def testDefine():
    define('x', 4)
    if lookup("x") != 4:
        return False
    define('x', 5)
    if lookup("x") != 5:
        return False
    return True

# test function for add
def testAdd():
    clear()
    opPush('x')
    opPush(2)
    add()
    if opPop() != 3: return False
    return True

# test fucntion for subtract
def testSub():
    clear()
    opPush(1)
    opPush(2)
    sub()
    if opPop() != 1: return False
    return True

# test fucntion for multiply
def testMul():
    opPush(1)
    opPush(2)
    mul()
    if opPop() != 2: return False
    return True

# test function for division
def testDiv():
    opPush(1)
    opPush(2)
    div()
    if opPop() != 2: return False
    return True

# test function for mod
def testMod():
    opPush(2)
    opPush(1)
    mod()
    if opPop() != 1: return False
    return True


# test function for length
def testLength():
    opPush([1, 2 ,3])
    length()
    if opPop() != 3: return False
    return True

# test function for get
def testGet():
    opPush(1)
    opPush([1, 2, 3])
    get()
    if opPop() != 2: return False
    return True

# test function for duplicate
def testDup():
    opPush(1)
    dup()
    op1 = opPop()
    op2 = opPop()
    if (op1 and op2) != 1: return False
    return True

# test function for exchange
def testExch():
    opPush(1)
    opPush(2)
    exch()
    if opPop() != 1 and opPop() != 2: return False
    return True

# test roll if positive
def testPosRoll():
    clear()
    opPush(3)
    opPush(2)
    opPush(1)
    opPush(2)
    opPush(3)
    roll()
    if opstack != [2, 1, 3]: return False
    return True

#test roll if negative
def testNegRoll():
    clear()
    opPush(3)
    opPush(2)
    opPush(1)
    opPush(-2)
    opPush(3)
    roll()
    if opstack != [1, 3, 2]: return False
    return True

# test function for copy
def testCopy():
    clear()
    opPush(3)
    opPush(2)
    opPush(2)
    copy()
    if opstack != [3, 2, 3, 2]: return False
    return True

# test function for clear
def testClear():
    clear()
    opPush(1)
    opPush(2)
    opPush(3)
    clear()
    dictPush({'x' : 2})
    if opstack != []: return False
    return True

# test function of begin
def testBegin():
    clear()
    opPush({'x' : 1})
    begin()
    if dictPop() != {'x' : 1}: return False
    return True

# test function for look up
def testLookup():
    opPush(3)
    opPush("/n")
    psDef()
    if lookup("n") != 3: return False
    return True

def testPsDef():
    opPush(3)
    opPush("/n")
    opPush(2)
    opPush("/c")
    psDef()
    if dictPop() != {'n' : 3, 'c' : 2}: return False
    return True

# Homework part B

# use to tokenize strings
def tokenize(s):
    retValue = re.findall(
        "/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    return retValue

# 2. Convert the token list to a code array

# puts elements into the list until it finds a '}'
def parseMatching(it):
    res = []
    # goes through the list add elements until it sees a '}'
    for c in it:
        if c == '}':
            return res
        elif c == '{': # this means that there is an inner code array
            res.append(parseMatching(it))
        else:
            # cast number into int if not does nothing
            try:
                c = int(c)
            except ValueError:
                pass
            # puts the values into the list
            res.append(c)
    return False

# parse the list and puts it into a list
def parse(s):
    # finds the first instance of '{'
    index = s.index('{') + 1
    # returns the list between the { }
    ret = parseMatching(iter(s[index:]))
    # the elements before { }
    lst = s[:index - 1]
    lst.append(ret)
    s.reverse()
    # adds the elements after the list
    index = s.index('}')
    backend = s[: index]
    backend.reverse()
    newlst = lst + backend
    # converts string list into lists
    newlst = convertList(newlst)
    # casts string into int if they need to be
    newlst = typecast(newlst)
    return newlst

# cast all of the numbers that needs to be ints
def typecast(s):
    newlst = []
    # goes through the list
    for c in s:
        # trys to cast into everything into ints if not do nothing
        try:
           c = int(c)
        except ValueError:
            pass
        except TypeError:
            pass
        # if it is a list then it is recursed called to convet the list of ints into ints
        if type(c) is list:
            c = typecast(c)
        # then appends it to the list
        newlst.append(c)
    return newlst

# converts a string list into an actual list
def convertList(s):
    newlst = []
    for c in s:
        if (type(c) is str) and (c[0] == '[' and c[-1] == ']'):
              newlst.append(c[1:-1].split(' '))
        elif type(c) is list:
            newlst.append(convertList(c))
        else:
            newlst.append(c)
    return newlst

# 4. Interpret the SPS code
# interprets the code arrays
def interpret(code): # code is a code array
    for i in code:
        if isinstance(i, int):
            opPush(i)
        # if it is a built in function
        elif isinstance(i, str):
            if i[0] == '/':
                opPush(i)
            elif i == 'add':
               add()
            elif i == 'sub':
                sub()
            elif i == 'mul':
                mul()
            elif i == 'div':
                div()
            elif i == 'mod':
                mod()
            elif i == 'get':
                get()
            elif i == 'length':
                length()
            elif i == 'dup':
                dup()
            elif i == 'exch':
                exch()
            elif i == 'pop':
                pop()
            elif i == 'roll':
                roll()
            elif i == 'copy':
                copy()
            elif i == 'clear':
                clear()
            elif i == 'stack':
                stack()
            elif i == 'dict':
                psDict()
            elif i == 'begin':
                begin()
            elif i == 'end':
                end()
            elif i == 'def':
                psDef()
            elif i == 'for':
                forLoop()
            elif i == 'forall':
                forAll()
            else:
                # it is a variable
                value = lookup(i)
                # if it is a list checks if it is either a code array or not
                if isinstance(value, list):
                    numArray = True
                    for i in value:
                        if type(i) is not int:
                            numArray = False
                            break
                    # if true push it onto to the stack
                    if numArray == True:
                        opPush(value)
                    else:
                        # if a code array then interpret it again
                        interpret(value)
                else:
                    opPush(value)
        else:
            # if it is a list and adds it
            opPush(i)

# the for loop
def forLoop():
    op1 = opPop() # operation
    op2 = opPop() # end
    op3 = opPop() # increment
    op4 = opPop() # start

    for i in range(op4, op2, op3):
        opPush(i)
        interpret(op1)

def forAll():
    op1 = opPop() # operations
    op2 = opPop() # list

    for i in op2:
        opPush(i)
        interpret(op1)

def interpreter(s):
    interpret(parse(tokenize(s)))

def testParse():
    if parse(tokenize(
        """
        /square {dup mul} def 1 square 2 square 3 square add add
        """
    )) != ['/square', ['dup', 'mul'], 'def', 1, 'square', 2, 'square', 3, 'square', 'add', 'add']:
        return False
    elif parse(tokenize("""
    /n 5 def 1 n -1 1 {mul} for
    """)) != ['/n', 5, 'def', 1, 'n', -1, 1, ['mul'], 'for']:
        return False
    elif parse(tokenize(
        """
        /sum {-1 0 {add} for} def
        0
        [1 2 3 4] length
        sum
        2 mul
        [1 2 3 4] {2 mull} forall
        add add add
        stack
        """)) != ['/sum', [-1, 0, ['add'], 'for'], 'forall', 'add', 'add', 'add', 'stack']:
        return False
    return True

def testInterpreter():
    interpreter(
        """
           /fact{
            0 dict
                    begin
                            /n exch def
                            1
                            n -1 1 {mul} for
                    end
            }def
            [1 2 3 4 5] dup 4 get pop
            length
            fact
            stack
        """)
    if opPop() != 120:
        return False
    return True

def testForAll():
    interpret([1, 2, 3, 4, [1, 2, 3], ['add', 'mul'], 'forall'])

    if opPop() != 37:
        return False
    return True

# main function
if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"

    if testParse():
        print(passedMsg % 'testParse')
    else:
        print(failedMsg % 'testParse ')

    if testInterpreter():
        print(passedMsg % 'testInterpreter')
    else:
        print(failedMsg % 'testInterpreter')

    if testForAll():
        print(passedMsg % 'testForAll')
    else:
        print(failedMsg % 'testForAll')
