'''
Created on Mar 8, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 7 Assignment

NOTE: My compiler is Python 3.5.0 | Anaconda 2.4.0.
'''


from week7_assignment import fileLength, parseData, writeToFile

# Testing with csv file.
print("The file has these lines: " + str(fileLength("D:\\LiClipse Workspace\\UCIIntroPython\\All_Live_Births_In_Illinois__1989-2009.csv")))

# Testing with txt file.
print("The file has these lines: " + str(fileLength("D:\\LiClipse Workspace\\UCIIntroPython\\us.state.1981_2013.19ages.race.adjusted.txt")))

parseData("D:\\LiClipse Workspace\\UCIIntroPython\\WeatherDataTest.txt")

print("Finished writing to file: " + writeToFile("D:\\LiClipse Workspace\\UCIIntroPython\\WriteFileTest.txt", ["today", "is", "my", "lucky", "day"]))
