"""_summary_
https://adventofcode.com/2023/day/3
Checking schematics for goblin engineering
"""
import inspect
import re
import os

from collections import Counter

def count_items(lst):
    return dict(Counter(lst))

# Example usage:
my_list = [1, 2, 3, 1, 2, 3, 4, 5]
item_counts = count_items(my_list)
print(item_counts)


def file_reader(file_path):
    """Reading and returning a files content"""
    with open(file_path, encoding="utf-8") as file:
        contents = file.readlines()
    return contents

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
INPUT_FILE_LINES = file_reader(os.path.join(PATH, 'day3.txt'))

def get_numbers_list(stringInput):
    return re.findall('[0-9]+', stringInput)

#missing diagonal check
def check_part_number(strNumber, currentLineIndex):
    #adjacentCounter = 0
    line = INPUT_FILE_LINES[currentLineIndex].rstrip('\n')
    subStringIndexStart = 0 if line.find(strNumber)  == 0 else line.find(strNumber) -1
    subStringIndexEnd = line.find(strNumber) + len(strNumber) + 1
    subLine = line[subStringIndexStart:subStringIndexEnd]
    #quickCheck
    lineList = []
    lineList.append(subLine)
    
    if currentLineIndex != 0 and currentLineIndex < len(INPUT_FILE_LINES)-1:
        lineList.append(INPUT_FILE_LINES[currentLineIndex+1][subStringIndexStart:subStringIndexEnd].rstrip('\n'))
        lineList.append(INPUT_FILE_LINES[currentLineIndex-1][subStringIndexStart:subStringIndexEnd].rstrip('\n'))
    elif currentLineIndex == 0:
        lineList.append(INPUT_FILE_LINES[currentLineIndex+1][subStringIndexStart:subStringIndexEnd].rstrip('\n'))
    else:
        lineList.append(INPUT_FILE_LINES[currentLineIndex-1][subStringIndexStart:subStringIndexEnd].rstrip('\n'))
       
    for line in lineList:
        if len(re.findall('[^0-9a-zA-Z.]',line)) > 0:
            return True
        
    return False

sumOfParts = 0
sumOfListNumbers = 0
for lineIndex in range(0,len(INPUT_FILE_LINES)):
    numbers = get_numbers_list(INPUT_FILE_LINES[lineIndex])
    intNumberList = []
    for n in numbers:
        intNumberList.append(int(n))
    intNumberList.sort()
    sumOfListNumbers += sum(intNumberList)
    #print(intNumberList)
    item_counts = count_items(intNumberList)
    for item, count in item_counts.items():
        if count > 1:
            print(f"The count of {item} is above 1.")
    for n in numbers:
        if check_part_number(n,lineIndex) == True:
            sumOfParts += int(n)
print(sumOfParts)
print(sumOfListNumbers)