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

# Might be easier if I had a set of indices per symbol and number
# Then I'd just have to compare the indices and maybe length of numbers
# Could create a set from each symbol index .*. like (2,3,4) and just say
# if numberIndex in range: countNumber or something

for lineIndex in range(0,len(INPUT_FILE_LINES)):
    line = INPUT_FILE_LINES[lineIndex].rstrip('\n')
    symbolsTuple = get_matches_as_tuple(line, REGEX_SYMBOLS_ONLY)
    numbersTuple = get_matches_as_tuple(line, REGEX_NUMBERS_ONLY)
    PARSED_LINES[lineIndex] = {"symbols" : symbolsTuple, "numbers" : numbersTuple}
        

#Logic goes here
numbersToParse = []
for currentIndex in range(0,len(PARSED_LINES)):
    if len(PARSED_LINES[currentIndex]["symbols"]) > 0:
        #print(PARSED_LINES[currentIndex])
        numbersList = {}
        numbersList[currentIndex] = PARSED_LINES[currentIndex]["numbers"]
        if currentIndex != 0 and currentIndex < len(PARSED_LINES)-1:
            numbersList[currentIndex+1] = PARSED_LINES[currentIndex+1]["numbers"]
            numbersList[currentIndex-1] = PARSED_LINES[currentIndex-1]["numbers"]
        elif currentIndex == 0:
            numbersList[currentIndex+1] = PARSED_LINES[currentIndex+1]["numbers"]
        else:
            numbersList[currentIndex-1] = PARSED_LINES[currentIndex-1]["numbers"]
        #print(PARSED_LINES[currentIndex]["symbols"],numbersList)
        for symbol in PARSED_LINES[currentIndex]["symbols"]:
            for symbolChar,symbolIndex in symbol.items():
                for numberListIndex,numberListTuples in numbersList.items():
                    for numberDict in numberListTuples:
                        for number in numberDict.keys():
                            numberIndex = numberDict[number]
                            #print(symbol,number,numberIndex,numberIndex+len(number))
                            if numberIndex <= symbolIndex <= numberIndex+len(number):
                                #print("Behind")
                                #print(numberListIndex,numberDict, symbol,number,numberIndex,numberIndex+len(number))
                                numbersToParse.append({numberListIndex : numberDict})
                                continue
                            if symbolIndex+1 == numberIndex or symbolIndex == numberIndex:
                                #print("Ahead")
                                #print(numberListIndex,numberDict, symbol,number,numberIndex,numberIndex+len(number))
                                numbersToParse.append({numberListIndex : numberDict})
                                continue         

finalNumber = []
for entry in numbersToParse:
    for valueDict in entry.values():
        for key in valueDict.keys():
            finalNumber.append(int(key))
            
print(sum(finalNumber))
                       
#needs to have duplicates checked or something by using a set       
#print(sum(set(numbersToParse)))
                                    
    #print(lineIndex, line)
    #print(lineIndex, symbolsTuple)
    #print(lineIndex, numbersTuple)
    #print("\n")
    #if len(resultsList) > 0:
    #    for result in resultsList:
    #        for char,index in result.items():
    #            print(char,index)
        #check if surrounding area contains above/below/diagonally any numeric value
        #if yes
        #run back to find the number
        #count numbers found this way



"""
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

"""