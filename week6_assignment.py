'''
Created on Mar 1, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 6 Assignment

NOTE: My compiler is Python 3.5.0 | Anaconda 2.4.0.
'''
from datetime import datetime, timedelta
from glob import glob


def days15(myDateStr):

    dateObj = datetime.strptime(myDateStr, '%Y%m%d')
    deltaObj = timedelta(days=1)

    dateList = [dateObj + deltaObj*i for i in range(15)]

    # If we want to print each element of the list in a new line, we use this:
    # http://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
    # This is for Python 3.x
    #print(*dateList, sep='\n')
    return dateList


# This version is really short. Items are stored in a list.
# The length of the list returns the number of items stored.
def countFiles1(globPattern):

    filePath = glob(globPattern)
    numberFiles = len(filePath)

    return numberFiles


# This version is longer as it uses a for loop, which would be useful to print
# each file, if required.
def countFiles2(globPattern):

    filePath = glob(globPattern)
    numberFiles = 0

    for fPath in filePath:
        # In case we need to print each file that matches the glob pattern.
        # print(fPath)
        numberFiles += 1

    return numberFiles
