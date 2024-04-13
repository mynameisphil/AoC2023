"""
https://adventofcode.com/2023/day/1
What is the sum of all of the calibration values?
"""
import inspect, os
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# Using readlines() https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
day1File = open(os.path.join(path, 'day1_test2.txt'), 'r')
inputList = day1File.readlines()

numbersMap = { 
              'one' : 1,
              'two' : 2, 
              'three' : 3,
              'four' : 4,
              'five' : 5,
              'six' : 6,
              'seven' : 7,
              'eight' : 8,
              'nine' : 9
              }
intTotalCalibration = 0

for input in inputList:
    if len(input) > 0:
        indexList = []
        indexMap = {}
        for number in numbersMap.keys():
            index = input.find(number)
            if index >= 0:
                indexMap[index] = numbersMap[number]
                indexList.append(index)
        letters = list(input)
        i = 0
        while i < len(input):
            if letters[i].isdigit():
                indexMap[i] = int(letters[i])
                indexList.append(i)
                break
            i += 1
        i = len(input)-1
        while i >= 0:
            if letters[i].isdigit():
                indexMap[i] = int(letters[i])
                indexList.append(i)
                break
            i -= 1
        indexList.sort()
        numberAsString = str(indexMap[indexList[0]]) + str(indexMap[indexList[len(indexList)-1]])
        print(input.rstrip('\n') + ' = ' + numberAsString +' - '  + str(indexMap) + ' - '  + str(indexList) + '\n')
        intTotalCalibration += int(numberAsString)   
print(intTotalCalibration)