""" Solution to Advent of Code, 2023 - Day 1 Puzzle 1 """
import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
FilePath = join(CurrentDir, "./input.txt")
TOTALCALIBRATION = 0

with open(FilePath, "+r", encoding="UTF8+") as input_file:
    lines = input_file.readlines()

for line in lines:
    x = re.findall(r'\d', line)
    TOTALCALIBRATION += ( int( x[0] + x[-1] ) )

print( TOTALCALIBRATION )
