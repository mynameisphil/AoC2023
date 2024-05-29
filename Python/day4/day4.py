"""_summary_
https://adventofcode.com/2023/day/4
Checking Scratchcards
"""
import inspect
import re
import os

def file_reader(file_path):
    with open(file_path, encoding="utf-8") as file:
        contents = file.readlines()
    return contents

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
INPUT_FILE_LINES = file_reader(os.path.join(PATH, 'day4_test.txt'))
REGEX_NUMBERS_ONLY = r"[0-9]+"
PART1_RESULT = 0
PART2_RESULT = 0
LIST_CARDS = []

class Card:
    def __init__(self, inputCard):
        self.Number = int(re.findall(REGEX_NUMBERS_ONLY, inputCard.split(':')[0])[0])
        self.luckyNumbers = set(map(int, re.findall(REGEX_NUMBERS_ONLY, inputCard.split(':')[1].split('|')[0])))
        self.cardNumbers = set(map(int, re.findall(REGEX_NUMBERS_ONLY, inputCard.split('|')[1])))
        self.winningNumbers = self.cardNumbers.intersection(self.luckyNumbers)
        self.Value = 0
        self.copyList = []
        if len(self.winningNumbers) == 1:
            self.Value = 1
        elif len(self.winningNumbers) > 1:
            self.Value = 1 << len(self.winningNumbers) - 1
        
    def __str__(self):
        return f"{self.Value}"

for line in INPUT_FILE_LINES:
    card = Card(line)
    LIST_CARDS.append(card)
    PART1_RESULT += card.Value

#Solve Part 1
print("Part 1:",PART1_RESULT)

#Solve Part 2
print("Part 2:",PART2_RESULT)
for card in LIST_CARDS: #init copies
    card.copyList = LIST_CARDS[card.Number:card.Number+len(card.winningNumbers)]
    copyStr = ""
    for copy in card.copyList:
        copyStr += " " + str(copy.Number)
    print(card.Number, copyStr)
