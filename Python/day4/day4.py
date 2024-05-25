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
INPUT_FILE_LINES = file_reader(os.path.join(PATH, 'day4.txt'))
REGEX_NUMBERS_ONLY = r"[0-9]+"

class Card:
    def __init__(self, inputCard):
        self.Number = re.findall(REGEX_NUMBERS_ONLY, inputCard.split(':')[0])
        self.luckyNumbers = set(map(int, re.findall(REGEX_NUMBERS_ONLY, inputCard.split(':')[1].split('|')[0])))
        self.cardNumbers = set(map(int, re.findall(REGEX_NUMBERS_ONLY, inputCard.split('|')[1])))
        self.winningNumbers = self.cardNumbers.intersection(self.luckyNumbers)
        self.cardValue = 0
        if len(self.winningNumbers) == 1:
            self.cardValue = 1
        elif len(self.winningNumbers) > 1:
            self.cardValue = 1 << len(self.winningNumbers) - 1
        
    def __str__(self):
        return f"{self.cardValue}"

totalWinningPoints = 0       

for line in INPUT_FILE_LINES:
    lineCard = Card(line)
    totalWinningPoints += lineCard.cardValue
    
print(totalWinningPoints)
    