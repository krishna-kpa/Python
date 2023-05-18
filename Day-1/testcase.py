# import testing functions
import  linearSearch
linear_locate_card = linearSearch.linear_locate_card

import binarySearch
binary_locate_card = binarySearch.binary_locate_card

# creating test cases
tests = []

# case-1 card in 3rd position
test1 = {
    'input':{
        'cards': [13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output':3
}

# case-2 card not in the list
test2 = {
    'input':{
        'cards': [13,11,10,7,4,3,1,0],
        'query': 12
    },
    'output':-1
}

# case-3 card in middle
test3 = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
}

# case-4 card is the last element
test4 = {
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
}

# case-5 cards contains just one element, card
test5 = {
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
}

# case-6 cards is empty
test6 = {
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
}

# case-7 card number can repeat in cards
test7 = {
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
}

# case-8 card occurs multiple times
test8 = {
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
}

# add your test case here and dont forget to append it in the tests

# appending all test cases to tests
tests.extend([test1,test2,test3,test4,test5,test6,test7,test8])



# testing function using test case
# For linear search
print("\n-------- Linear Seach result --------\n")
testResult = []
result = list()
for i in range(len(tests)):
    result.append(list(linear_locate_card(tests[i]["input"]['cards'],tests[i]["input"]['query'])))
    if(result[i][0] == tests[i]["output"]):
        testResult.append([True,result[i][1]])
    else:
        testResult.append([False,result[i][1]])
for i in range(len(testResult)):
    caseNo = i+1
    print("Test "+str(caseNo)+" = "+str(testResult[i][0])+", loop ran "+str(testResult[i][1])+" , Cards : "+str(tests[i]["input"]['cards'])+" , Query : "+str(tests[i]["input"]['query'])+" , Expected Output : "+str(tests[i]["output"])+" , Your Output : "+str(result[i][0]))



# For Binary search

print("\n-------- Binary Seach result --------\n")
testResult = []
result = list()
for i in range(len(tests)):
    result.append(list(binary_locate_card(tests[i]["input"]['cards'],tests[i]["input"]['query'])))
    if(result[i][0] == tests[i]["output"]):
        testResult.append([True,result[i][1]])
    else:
        testResult.append([False,result[i][1]])
for i in range(len(testResult)):
    caseNo = i+1
    print("Test "+str(caseNo)+" = "+str(testResult[i][0])+", loop ran "+str(testResult[i][1])+" , Cards : "+str(tests[i]["input"]['cards'])+" , Query : "+str(tests[i]["input"]['query'])+" , Expected Output : "+str(tests[i]["output"])+" , Your Output : "+str(result[i][0]))
print('\n')