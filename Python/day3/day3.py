"""_summary_
https://adventofcode.com/2023/day/3
Checking schematics for goblin engineering
"""
import inspect
import re
import os

def file_reader(file_path):
    with open(file_path, encoding="utf-8") as file:
        contents = file.readlines()
    return contents

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
INPUT_FILE_LINES = file_reader(os.path.join(PATH, 'day3.txt'))

REGEX_SYMBOLS_ONLY = r"[^0-9.]"
REGEX_NUMBERS_ONLY = r"[0-9]+"

PARSED_LINES = {}

def get_matches_list(stringInput, pattern):
    return re.findall(pattern, stringInput)

def get_matches_as_tuple(input_string, pattern):
    matches = re.finditer(pattern, input_string)
    match_indices = []
    for match in matches:
        matched_char = match.group()
        index = match.start()
        match_indices.append({matched_char : index})
    return tuple(match_indices)


def solve_part1():
    #Logic goes here - this would have been a ton easier if I had opted to use a proper data structure instead
    for lineIndex in range(0,len(INPUT_FILE_LINES)):
        line = INPUT_FILE_LINES[lineIndex].rstrip('\n')
        symbolsTuple = get_matches_as_tuple(line, REGEX_SYMBOLS_ONLY)
        numbersTuple = get_matches_as_tuple(line, REGEX_NUMBERS_ONLY)
        PARSED_LINES[lineIndex] = {"symbols" : symbolsTuple, "numbers" : numbersTuple}
        
    numbersToParse = []
    for currentIndex in range(0,len(PARSED_LINES)):
        if len(PARSED_LINES[currentIndex]["symbols"]) > 0:
            numbersList = {}
            numbersList[currentIndex] = PARSED_LINES[currentIndex]["numbers"]
            if currentIndex != 0 and currentIndex < len(PARSED_LINES)-1:
                numbersList[currentIndex+1] = PARSED_LINES[currentIndex+1]["numbers"]
                numbersList[currentIndex-1] = PARSED_LINES[currentIndex-1]["numbers"]
            elif currentIndex == 0:
                numbersList[currentIndex+1] = PARSED_LINES[currentIndex+1]["numbers"]
            else:
                numbersList[currentIndex-1] = PARSED_LINES[currentIndex-1]["numbers"]
            for symbol in PARSED_LINES[currentIndex]["symbols"]:
                for symbolChar,symbolIndex in symbol.items():
                    for numberListIndex,numberListTuples in numbersList.items():
                        for numberDict in numberListTuples:
                            for number in numberDict.keys():
                                numberIndex = numberDict[number]
                                if numberIndex <= symbolIndex <= numberIndex+len(number):
                                    numbersToParse.append({numberListIndex : numberDict})
                                    continue
                                if symbolIndex+1 == numberIndex or symbolIndex == numberIndex:
                                    numbersToParse.append({numberListIndex : numberDict})
                                    continue         

    finalNumber = []
    for entry in numbersToParse:
        for valueDict in entry.values():
            for key in valueDict.keys():
                finalNumber.append(int(key))
                
    print(sum(finalNumber))

def solve_part2():
    #Logic goes here - this would have been a ton easier if I had opted to use a proper data structure instead
    for lineIndex in range(0,len(INPUT_FILE_LINES)):
        line = INPUT_FILE_LINES[lineIndex].rstrip('\n')
        symbolsTuple = get_matches_as_tuple(line, REGEX_SYMBOLS_ONLY)
        numbersTuple = get_matches_as_tuple(line, REGEX_NUMBERS_ONLY)
        PARSED_LINES[lineIndex] = {"symbols" : symbolsTuple, "numbers" : numbersTuple}
        
    numbersToParse = []
    for currentIndex in range(0,len(PARSED_LINES)):
        if len(PARSED_LINES[currentIndex]["symbols"]) > 0:
            numbersList = {}
            numbersList[currentIndex] = PARSED_LINES[currentIndex]["numbers"]
            if currentIndex != 0 and currentIndex < len(PARSED_LINES)-1:
                numbersList[currentIndex+1] = PARSED_LINES[currentIndex+1]["numbers"]
                numbersList[currentIndex-1] = PARSED_LINES[currentIndex-1]["numbers"]
            elif currentIndex == 0:
                numbersList[currentIndex+1] = PARSED_LINES[currentIndex+1]["numbers"]
            else:
                numbersList[currentIndex-1] = PARSED_LINES[currentIndex-1]["numbers"]
            for symbol in PARSED_LINES[currentIndex]["symbols"]:
                partNumber = []
                for symbolChar,symbolIndex in symbol.items():
                    if symbolChar == "*":
                        for numberListIndex,numberListTuples in numbersList.items():
                            for numberDict in numberListTuples:
                                for number in numberDict.keys():
                                    numberIndex = numberDict[number]
                                    if numberIndex <= symbolIndex <= numberIndex+len(number):
                                        partNumber.append(int(number))
                                        continue
                                    if symbolIndex+1 == numberIndex or symbolIndex == numberIndex:
                                        partNumber.append(int(number))
                                        continue         
                if len(partNumber) == 2:
                    numbersToParse.append(int(partNumber[0]*partNumber[1]))
    print(sum(numbersToParse))
    
solve_part1()
solve_part2()