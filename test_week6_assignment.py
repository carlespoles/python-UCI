'''
Created on Mar 1, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 6 Assignment

NOTE: My compiler is Python 3.5.0 | Anaconda 2.4.0.
'''

from week6_assignment import days15, countFiles1, countFiles2

# The string we pass must have this order: yyyymmdd.
print(*days15('20160301'), sep='\n')
print('======================')
# Note that for windows machines, we need to use double \.
print('Number of files that match our criteria: ' + str(countFiles1('C:\\*.txt')))
print('======================')
print('Number of files that match our criteria: ' + str(countFiles2('C:\\*.txt')))
