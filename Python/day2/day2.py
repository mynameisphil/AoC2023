"""_summary_
https://adventofcode.com/2023/day/2
Check list of games if they are valid / possible
"""
import inspect
import os

def file_reader(file_path):
    """Reading and returning a files content"""
    with open(file_path, encoding="utf-8") as file:
        contents = file.readlines()
    return contents

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
INPUT_FILE_LINES = file_reader(os.path.join(PATH, 'day2.txt'))

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

GAMES_VALID = 0

def check_game_valid(input_map):
    """Function return boolean if game is valid"""
    if input_map['red'] > RED_CUBES:
        return False
    if input_map['green'] > GREEN_CUBES:
        return False
    if input_map['blue'] > BLUE_CUBES:
        return False
    return True

for gameLine in INPUT_FILE_LINES:
    gameId = int(gameLine.rstrip('\n').split(':')[0].split(' ')[1])
    gameList = gameLine.rstrip('\n').split(':')[1].split(';')
    gameValid = True
    for game in gameList:
        for subGame in game.split(','):
            cubeMap = {'red':0,'green':0,'blue':0}
            cubes = int(subGame.strip().split(' ')[0])
            color = subGame.strip().split(' ')[1]
            cubeMap[str(color)] = cubeMap[str(color)] + cubes
            if check_game_valid(cubeMap) is False:
                gameValid = False
                break
    if gameValid:
        GAMES_VALID += gameId
print('Valid games shown: ' + str(GAMES_VALID))
#EoF
