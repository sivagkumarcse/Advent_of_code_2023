#!/usr/bin/python3
import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
FilePath = join(CurrentDir, "./input.txt")

file = open( FilePath, "+r" )
lines = file.readlines()

greenPattern = r'(\d+) green'
bluePattern = r'(\d+) blue'
redPattern = r'(\d+) red'
gamePattern = r'Game (\d+):'

# 12 red cubes, 13 green cubes, and 14 blue cubes
ActualGreen = 13
ActualRed = 12
ActualBlue = 14

Answer = 0

def findMax(list):
    tempMax = 0
    for i in list:
        iVal = int(i)
        if ( tempMax <= iVal ):
            tempMax = iVal
    return (tempMax)

for line in lines:
    greenList = re.findall(greenPattern, line)
    redList = re.findall(redPattern, line)
    blueList = re.findall(bluePattern, line)
    game = re.findall(gamePattern, line)

    greenMax = findMax(greenList)
    redMax = findMax(redList)
    blueMax = findMax(blueList)

    if ( greenMax <= ActualGreen and blueMax <= ActualBlue 
         and redMax <= ActualRed ):
        Answer += int(game[0])

print(Answer)