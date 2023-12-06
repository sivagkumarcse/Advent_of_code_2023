#!/usr/bin/python3
from Day5lib import *
import re

class ClosestLocationFinder(Day5lib):

    seed2soil = []
    soil2fert = []
    fert2watr = []
    watr2lght = []
    lght2temp = []
    temp2humd = []
    humd2loct = []
    inputSeeds = []

    inputArray = [inputSeeds, seed2soil, soil2fert, fert2watr, watr2lght,
                  lght2temp, temp2humd, humd2loct]

    def __init__(self):
        pass
    
    def run(self):
        self.main()

    def checkLocneeded(self, loc, tableIndex):
        #print(loc, tableIndex)
        if ( tableIndex == 1 ):
            for seedSeries in range (0, int(len(self.inputArray[0])/2)):
                if (loc in range (self.inputArray[0][seedSeries*2], \
                    self.inputArray[0][seedSeries*2] + self.inputArray[0][(seedSeries*2)+1] - 1)):
                    print(f"Selected seed is {loc}")
                    return True
            return False
        else:
            table = self.inputArray[tableIndex-1]
            providedmap = False
            for entry in table:
                if (loc in range(entry[0], entry[0] + entry[2]) ):
                    locIndex = loc - entry[0]
                    providedmap = True
                    nextkey = entry[1] + locIndex
                    break

            if (providedmap == False):
                nextkey = loc

            return ( self.checkLocneeded(nextkey, tableIndex-1) )

    def main(self):
        # Use SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.readFileContent(INPUT_LOC.ORIGINAL_INPUT)
        arrInd = -1
        for line in content:
            match = ( re.findall(r'([\d]+)', line) )
            if "seeds:" in line:
                arrInd += 1
                match = list(map(int, match))
                self.inputArray[arrInd] = match

            elif "map:" in line:
                arrInd += 1

            elif (len(match) != 0 and arrInd!= -1 ):
                #Convert text input to int list
                match = list(map(int, match))
                self.inputArray[arrInd].append(match)

        # Find possible location max
        maxLoc = 0
        for locArray in self.humd2loct:
            maxLoc = max( maxLoc, (locArray[0] + locArray[2] - 1) )
            maxLoc = max( maxLoc, (locArray[1] + locArray[2] - 1) )

        # Do reverse search from location 1 to maxLoc
        tableLen = len(self.inputArray)
        for location in range(0, maxLoc+1):
            detected = self.checkLocneeded(location, tableLen)
            if(detected):
                print(f"Min Location is {location}")
                break

if __name__ == "__main__":
    closestLocationFinder = ClosestLocationFinder()
    closestLocationFinder.run()