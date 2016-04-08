'''
Created on Feb 8, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 3 Assignment

NOTE: My compiler is Python 3.5.0 |Anaconda 2.4.0.
'''
# Question 1.
for x in range(10):
    print(x)

# Question 2.
for x in range(10):
    if x == 0:
        print('zero')
    elif (x % 2) == 0:
        print('even')
    else:
        print('odd')

# Question 3.
myVar = 2.0

while(myVar <= 100):
    myVar = myVar * 1.65

print(myVar)
