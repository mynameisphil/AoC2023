"""
https://adventofcode.com/2023/day/1
What is the sum of all of the calibration values?
"""
import inspect
import os
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# Using readlines() https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
day1File = open(os.path.join(path, 'day1.txt'), 'r')
inputList = day1File.readlines()

numbersMap = {'one' : 1,
              'two' : 2, 
              'three' : 3,
              'four' : 4,
              'five' : 5,
              'six' : 6,
              'seven' : 7,
              'eight' : 8,
              'nine' : 9}
TOTALCALIBRATION = 0

for line in inputList:
    if len(line) > 0:
        indexList = []
        indexMap = {}
        for number, value in numbersMap.items():
            index = line.find(number)
            if index >= 0:
                indexMap[index] = value
                indexList.append(index)
            index = line.rfind(number)
            if index >= 0:
                indexMap[index] = value
                indexList.append(index)
        letters = list(line)
        i = 0
        while i < len(line):
            if letters[i].isdigit():
                indexMap[i] = int(letters[i])
                indexList.append(i)
                break
            i += 1
        i = len(line)-1
        while i >= 0:
            if letters[i].isdigit():
                indexMap[i] = int(letters[i])
                indexList.append(i)
                break
            i -= 1
        indexList.sort()
        TOTALCALIBRATION += int(str(indexMap[indexList[0]]) + str(indexMap[indexList[len(indexList)-1]]))
        
print(TOTALCALIBRATION)