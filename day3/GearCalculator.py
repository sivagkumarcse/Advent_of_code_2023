#!/usr/bin/python3
import re
from Day3lib import *

class GearCalulator(Day3lib):
    PNpattern = re.compile( r'(\d+)' )
    GearPair = {}
    
    def __init__(self):
        pass
    
    def run(self):
        self.main()

    def main(self):
        lineNu = 0
        sumGearRatio = 0
        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day3lib.readFileContent(self, INPUT_LOC.ORIGINAL_INPUT)
        if not content:
            return(0)

       # For every line
        for line in content:
            # For every Part number in a line
            for pn in self.PNpattern.finditer( line ):
                indexList = []
                indexListTemp = []

                for i in range( pn.span()[0], pn.span()[1] ):
                    if ( i == pn.span()[0] ) or \
                       ( i == pn.span()[1] - 1):
                        corner = True
                    else:
                        corner = False
                    indexList.extend( self.findSurroundingIndices
                                      ( lineNu, i, 
                                        self.maxRow, 
                                        self.maxColumn, 
                                        corner=corner ) )
                
                # Remove duplicate indices to check
                for item in indexList:
                    if item not in indexListTemp:
                        indexListTemp.append(item)
                indexList = indexListTemp
                indexListTemp = None

                # Check if the part number has * surrounding it
                for indices in indexList:
                    if self.GearChecker(content[indices[0]][indices[1]]):

                        # Create a dictonary with index of '*' as key
                        dictTuple = tuple([indices[0],indices[1]])
                        if dictTuple in self.GearPair.keys():
                            self.GearPair[dictTuple].append(int(pn.groups()[0]))
                        else:
                             self.GearPair[dictTuple] = [int(pn.groups()[0])]
                        break
            lineNu += 1

        # We have the GearPair, multiply and find the value if list size is 2
        for key in self.GearPair:
        #    print(key, "->", self.GearPair[key])
            gearList = self.GearPair[key]
            if ( len(gearList) == 2 ):
                sumGearRatio += gearList[0] * gearList[1]

        print("Output is " + str(sumGearRatio))
        return(sumGearRatio)   

if __name__ == "__main__":
    gearCalulator = GearCalulator()
    gearCalulator.run()