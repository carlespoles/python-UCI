'''
Created on Mar 8, 2016

@author: Carles Poles-Mielgo

UCI - Introduction to Python

Week 7 Assignment

NOTE: My compiler is Python 3.5.0 | Anaconda 2.4.0.
'''


def fileLength(filePath):
    with open(filePath, "r") as f:
        countLines = 0
        for line in f:
            countLines += 1

        return countLines


def parseData(filePath):
    weatherDataDictionary = {}
    with open(filePath, "r") as f:
        for line in f:
            line = line.strip()
            weatherStation = line[0:0+8]
            weatherTemperature = line[8:8+3]
            weatherHumidity = line[11:11+2]

            if not(weatherStation in weatherDataDictionary):
                weatherDataDictionary[weatherStation] = {}
                weatherDataDictionary[weatherStation] = [weatherTemperature,
                                                         weatherHumidity]

        for key, value in weatherDataDictionary.items():

            # Ideally, we want a return statement.
            print("Station ID " + str(key) + " data collected: " +
                  str(value) + "\n")

            print("Station ID " + str(key) + " has a temperature of " +
                  str(value[0]) + " Celsius, and a relative humidity of " +
                  str(value[1]) + "%" + "\n")


def writeToFile(filePath, linesToWrite):
    with open(filePath, "w") as f:
        for line in linesToWrite:
            line += "\n"
            f.write(line)

        return filePath
