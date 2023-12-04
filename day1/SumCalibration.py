import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
FilePath = join(CurrentDir, "./input.txt")
TotalCalibration = 0

file = open( FilePath, '+r' )
lines = file.readlines()

for line in lines:
    x = re.findall(r'\d', line)
    TotalCalibration += ( int( x[0] + x[-1] ) )

print( TotalCalibration )