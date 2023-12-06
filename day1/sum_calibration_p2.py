""" Solution to Advent of Code, 2023 - Day 1 Puzzle 2 """
import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
FilePath = join(CurrentDir, "./input.txt")
TOTALCALIBRATION = 0
MYRE = r'((?=((one|t(wo|hree)|f(our|ive)|s(ix|even)|eight|nine)|\d)))'
#?= is for forward append to handle cases like oneight and twone

digitDict = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5, 
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    }

def convert_int(my_str):
    """ Check if the input is a valid digit, if not look in lookup tabe"""
    if my_str.isdigit():
        return int(my_str)
    return digitDict[my_str]

with open(FilePath, "+r", encoding="UTF8+") as input_file:
    lines = input_file.readlines()

for line in lines:
    x = re.findall(MYRE, line)
    TOTALCALIBRATION +=  ( convert_int( x[0][1] ) * 10 ) + convert_int( x[-1][1] )

print( TOTALCALIBRATION )
