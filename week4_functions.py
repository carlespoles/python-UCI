'''
Created on Feb 14, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 4 Assignment

NOTE: My compiler is Python 3.5.0 |Anaconda 2.4.0.
'''


def repeatString(myString, myNumber):
    finalString = ""
    for x in range(myNumber):
        finalString = finalString + myString
    return finalString


def multiplyNumbers(tupleOfNumbers):
    tupleLength = len(tupleOfNumbers)
    y = 1
    for x in range(tupleLength):
        y = y * tupleOfNumbers[x]
    return y


def filterList(stringList, string):
    listLength = len(stringList)
    for x in range(listLength):
        if (string in stringList):
            stringList.remove(string)
    return stringList


def list2Unique(inputList):
    # We declare a new empty list that will contain the unique elements of
    # the original list argument 'inputList'
    # Other data structures like sets DO NOT keep the order of the
    # unique elements.
    distinctList = []
    # We loop through all elements in inputList.
    for x in inputList:
        # If the element is not found, then add it to the new list.
        # Therefore, duplicates won't be added AND order will be preserved.
        if x not in distinctList:
            distinctList.append(x)
    return distinctList
