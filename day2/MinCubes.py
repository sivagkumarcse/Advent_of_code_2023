#!/usr/bin/python3
import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
InputFilePath = join(CurrentDir, "./input.txt")
SampleInputFilePath = join(CurrentDir, "./input_sample.txt")

file = open( InputFilePath, "+r" )
lines = file.readlines()

greenPattern = r'(\d+) green'
bluePattern = r'(\d+) blue'
redPattern = r'(\d+) red'

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

    greenMax = findMax(greenList)
    redMax = findMax(redList)
    blueMax = findMax(blueList)

    Answer += (greenMax * redMax * blueMax )

print(Answer)