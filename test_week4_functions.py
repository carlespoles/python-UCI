'''
Created on Feb 14, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 3 Assignment

NOTE: My compiler is Python 3.5.0 |Anaconda 2.4.0.
'''
from week4_functions import repeatString, multiplyNumbers, filterList, \
    list2Unique

stringTest = 'hello'
numberTest = 4

print(repeatString(stringTest, numberTest))

tupleTest = (3, 4, 78)

print(multiplyNumbers(tupleTest))

stringListTest = ['hello', 'xyz', 'zara', 'abc', 'xyz']
stringInListTest = 'xyz'

print(filterList(stringListTest, stringInListTest))

inputListTest = [5, 5, 'apple', 'pizza', 'apple']

print(list2Unique(inputListTest))
