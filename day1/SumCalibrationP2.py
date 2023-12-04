import re
from os.path import dirname, join

CurrentDir = dirname(__file__)
FilePath = join(CurrentDir, "./input.txt")
TotalCalibration = 0
myRe = r'((?=((one|t(wo|hree)|f(our|ive)|s(ix|even)|eight|nine)|\d)))'
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
def convertInt(myStr):
    if myStr.isdigit():
        return (int(myStr))
    else:
        return ( digitDict[myStr] )

file = open( FilePath, '+r' )
lines = file.readlines()

for line in lines:
    x = re.findall(myRe, line)
    TotalCalibration +=  ( convertInt( x[0][1] ) * 10 ) + convertInt( x[-1][1] )

print( TotalCalibration )