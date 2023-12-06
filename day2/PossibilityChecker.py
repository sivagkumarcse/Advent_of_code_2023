#!/usr/bin/python3
import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
FilePath = join(CurrentDir, "./input.txt")

with open(FilePath, encoding="utf-8") as file:
    lines = file.readlines()

GREENPATTERN = r'(\d+) green'
BLUEPATTERN = r'(\d+) blue'
REDPATTERN = r'(\d+) red'
GAMEPATTERN = r'Game (\d+):'

# 12 red cubes, 13 green cubes, and 14 blue cubes
ACTUALGREEN = 13
ACTUALRED = 12
ACTUALBLUE = 14

ANSWER = 0

def find_max(arg_list):
    """Simple function to return max variable in list"""
    temp_max = 0
    for i in arg_list:
        ival = int(i)
        temp_max = max(temp_max, ival)
    return temp_max

for line in lines:
    greenList = re.findall(GREENPATTERN, line)
    redList = re.findall(REDPATTERN, line)
    blueList = re.findall(BLUEPATTERN, line)
    game = re.findall(GAMEPATTERN, line)

    GMAX = find_max(greenList)
    RMAX = find_max(redList)
    BMAX = find_max(blueList)

    if ( GMAX <= ACTUALGREEN and BMAX <= ACTUALBLUE
         and RMAX <= ACTUALRED ):
        ANSWER += int(game[0])

print(ANSWER)
