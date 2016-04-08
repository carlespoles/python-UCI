'''
Created on Feb 22, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 5 Assignment

NOTE: My compiler is Python 3.5.0 |Anaconda 2.4.0.
'''

# 1.

myWordList = ['apple', 'orange', 'banana']

myNewWordList = map(lambda x: '_' + x, myWordList)

# http://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x
# We need to use list in order to print the result of a map function, otherwise
# we would get this printout => <map object at 0x013ED250> by using
# print (myNewWordList)

print(list(myNewWordList))

# 2.

myStateList = ['CA', 'OR', 'NY', 'OR']

myNewStateList = filter(lambda x: x != 'OR', myStateList)

# As with printing maps, same happens with filters as described above.

print(list(myNewStateList))

# 3.

myNumberList = [1, 2, 3, 4, 5]

myNewNumberList = [x*3 for x in myNumberList]

print(myNewNumberList)

# 4.

listOfWords = ['love', 'the', 'outdoors', 'with', 'passion']

wordsToRemove = ['the', 'width', 'of', 'a']

newListOfWords = [x for x in listOfWords if x not in wordsToRemove]

print(newListOfWords)
