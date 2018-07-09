# Kimi Phan
# Homework 1
# Unix/Mac ios

# debugging function that can be turned on and off by changing a single variable
debugging = True
def debug(*s):
    if debugging:
        print(*s)

# 1. Warmup - cryptDict() and decrypt()

# encrypts the string
def cryptDict(s1, s2):
    # empty dictionary is declared
    diction = {}
    for i, j in zip(s1, s2):
        # fills the dictionary with letters from s1 and s2
        diction[i] = j
    # returns the dictionary filled with letters from s1 and s2
    return diction

# decrypts the string
def decrypt(cdict, s):
    newString = ""
    for i in s:
        # looks up each letter in s and matches up with it's letter in the dictionary
        newString += cdict.get(i, i)
    # returns the decrypted string
    return newString

# testing code
def testDecrypt():
    cdict = cryptDict('abc', 'xyz')
    revcdict = cryptDict('xyz', 'abc')
    tests = "Now I know my abc’s"
    answer = "Now I know my xyz’s"
    if decrypt(cdict, tests) != answer:
        return False
    if decrypt(revcdict, decrypt(cdict, tests)) != "Now I know mb abc’s":
        return False
    if decrypt(cdict,'') != '':
        return False
    if decrypt(cryptDict('', ''), 'abc') != 'abc':
        return False
    return True

# 2. charCount()

# Counts the number of times that each character appears in a given string
def charCount(S):
    # empty dictionary is declared
    dict = {}
    for i in S:
        # spaces are not included
        if i != ' ':
            if i in dict.keys():
                # if it is in the dictionary then the character number is incremented
                dict[i] = dict.get(i) + 1
            else:
                # if it is not in the dictionary then it will be added
                dict[i] = 1
    # converts the dictionary into a list and orders them by the number of times it shows up first
            # then by the character
    numOfChars = sorted(list(dict.items()), key = lambda x: [x[1], x[0]])
    # returns a list of tuples
    return numOfChars

# testing code
def testCount():
    test = 'Cpts355 --- Assign1'
    answer = [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3) ]
    # test function overall
    if charCount(test) != answer:
        return False
    # tests for an empty string
    if charCount('') != []:
        return False
    # test for a space
    if charCount(' ') != []:
        return False
    # test to see if it orders the tuples by the first element
    if charCount('acefdb') != [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]:
        return False
    # test to see if it orders the tuples by the second element
    if charCount('abbbccdef') != [('a', 1), ('d', 1), ('e', 1), ('f', 1), ('c', 2), ('b', 3)]:
        return False
    return True

# 3. dictAddup()

def dictAddup(d):
    # empty dictionary to hold all of the hours
    totalHours = {}
    # outer loops to go through the days in the dictionary
    for days, classes in d.items():
        # inners loop to go through the classes
        for key in classes:
            # adds up all the hours for each class
            totalHours[key] = classes[key] + totalHours.get(key, 0)
    # returns a dictionary total hours studied for each class
    return totalHours

def testAddup():
    test = {'Monday':{'355':2,'451':1,'360':2},'Tuesday':{'451':2,'360':3}, 'Thursday':{'355':3,'451':2,'360':3}, 'Friday':{'355':2},
            'Sunday':{'355':1,'451':3,'360':1}}
    answer = {'355':8,'451':8,'360':9}
    # test the function overall
    if dictAddup(test) != answer:
        return False
    # test for an empty dictionary
    if dictAddup({}) != {}:
        return False
    # test to see if the hours still gets added up the same with different ordered classes
    if dictAddup({'Monday':{'322':2,'317':3}, 'Friday':{'317':1, '322':4}}) != {'322': 6, '317':4}:
        return False
    return True

debug(testDecrypt(), testCount(), testAddup())

# main function
if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    # testing cryptDict() and decrypt()
    if testDecrypt():
        print (passedMsg % 'testDecrypt')
    else:
        print (failedMsg % 'testDecrypt')
    # testing charCount()
    if testCount():
        print (passedMsg % 'testCount')
    else:
        print (failedMsg % 'testCount')
    # testing dictAddup()
    if testAddup():
        print (passedMsg % 'testAddup')
    else:
        print (failedMsg % 'testAddup')