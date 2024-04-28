"""_summary_
https://adventofcode.com/2023/day/3
Checking schematics for goblin engineering
"""
import inspect
import re
import os

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
    adjacentCounter = 0
    line = INPUT_FILE_LINES[currentLineIndex]
    subStringIndexStart = 0 if line.find(strNumber)  == 0 else line.find(strNumber) -1
    subStringIndexEnd = line.find(strNumber) + len(strNumber) + 1
    subLine = line[subStringIndexStart:subStringIndexEnd]
    #quickCheck
    if subLine[0].isdigit() == False and subLine[0] != ".":
        return True
    if subLine[-1].isdigit() == False and subLine[-1] != ".":
        return True
    if currentLineIndex != 0 and currentLineIndex < len(INPUT_FILE_LINES)-1:
        lineAbove = INPUT_FILE_LINES[currentLineIndex-1][subStringIndexStart:subStringIndexEnd]
        lineBelow = INPUT_FILE_LINES[currentLineIndex+1][subStringIndexStart:subStringIndexEnd]
        if len(lineAbove) != lineAbove.count('.'):
            return True
        if len(lineBelow) != lineBelow.count('.'):
            return True
    elif currentLineIndex == 0:
        lineBelow = INPUT_FILE_LINES[currentLineIndex+1][subStringIndexStart:subStringIndexEnd]
        if len(lineBelow) != lineBelow.count('.'):
            return True
    else:
        lineAbove = INPUT_FILE_LINES[currentLineIndex-1][subStringIndexStart:subStringIndexEnd]
        if len(lineAbove) != lineAbove.count('.'):
            return True
    if adjacentCounter > 0:
        return True
    """
    if currentLineIndex != 0 and currentLineIndex < len(INPUT_FILE_LINES)-1:
        lineAbove = INPUT_FILE_LINES[currentLineIndex-1][subStringIndexStart:subStringIndexEnd]
        lineBelow = INPUT_FILE_LINES[currentLineIndex+1][subStringIndexStart:subStringIndexEnd]
        for index, char in enumerate(subLine):
            if lineAbove[index] != ".":
                adjacentCounter += 1
            if lineBelow[index] != ".":
                adjacentCounter += 1
    elif currentLineIndex == 0:
        lineBelow = INPUT_FILE_LINES[currentLineIndex+1][subStringIndexStart:subStringIndexEnd]
        for index, char in enumerate(subLine):
            if lineBelow[index] != ".":
                adjacentCounter += 1
    else:
        lineAbove = INPUT_FILE_LINES[currentLineIndex-1][subStringIndexStart:subStringIndexEnd]
        for index, char in enumerate(subLine):
            if lineAbove[index] != ".":
                adjacentCounter += 1
    if adjacentCounter > 0:
        return True
    """
    return False

sumOfParts = 0
for lineIndex in range(0,len(INPUT_FILE_LINES)):
    numbers = get_numbers_list(INPUT_FILE_LINES[lineIndex])
    for n in numbers:
        if check_part_number(n,lineIndex) == True:
            sumOfParts += int(n)
print(sumOfParts)
"""
sumOfParts = 0
for lineIndex in range(0,len(INPUT_FILE_LINES)):
    currentLine = INPUT_FILE_LINES[lineIndex]
    numberList = []
    number = ""
    for index, char in enumerate(currentLine):
        if char.isdigit():
            number += char
        elif len(number) > 0:
            numberList.append(number)
            if check_part_number(number,lineIndex) == True:
                sumOfParts += int(number)
            number = ""
    #print(numberList)
print(sumOfParts)
"""          

"""

"""
"""
def find_indices(list_to_check, item_to_find):
    indices = []
    for i, x in enumerate(list_to_check):
        if x == item_to_find:
            indices.append(i)
    return indices
"""
"""
lineIndex = 0
while lineIndex  < len(INPUT_FILE_LINES):
    #getNumbers
    numberList = get_numbers_list(INPUT_FILE_LINES[lineIndex])
    if len(numberList) > 0:
        for number in numberList:
            print(number)
    else:
        print("Empty line")
    lineIndex += 1
"""


#a_list = [1, 2, 3, 4, 1, 2, 1, 2, 3, 4]
#print(find_indices(a_list, 1))  # Returns: [0, 4, 6]