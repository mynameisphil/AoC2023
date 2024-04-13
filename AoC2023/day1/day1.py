"""
https://adventofcode.com/2023/day/1
What is the sum of all of the calibration values?
"""
import inspect, os
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# Using readlines() https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
day1File = open(os.path.join(path, 'day1.txt'), 'r')
inputList = day1File.readlines()
intTotalCalibration = 0
for input in inputList:
    if len(input) > 0:
        number = ''
        letters = list(input)
        i = 0
        while i < len(input):
            if letters[i].isdigit():
                number += letters[i]
                break
            i += 1
        i = len(input)-1
        while i >= 0:
            if letters[i].isdigit():
                number += letters[i]
                break
            i -= 1
        intTotalCalibration += int(number)   
print(intTotalCalibration)