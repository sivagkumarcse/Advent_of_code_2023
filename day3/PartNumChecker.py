#!/usr/bin/python3
from Day3lib import *
import re

PNpattern = re.compile( r'(\d+)' )
sum = 0

class PartNumChecker(Day3lib):
    def __init__(self):
        pass
    
    def run(self):
        self.main()

    # Main implementation
    def main(self):
        lineNu = 0
        sum = 0

        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day3lib.readFileContent(self, INPUT_LOC.ORIGINAL_INPUT)
        if not content:
            return(0)

        # For every line
        for line in content:
            # For every Part number in a line
            for pn in PNpattern.finditer( line ):
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

                # Check if special character is surrounding the part number
                for indices in indexList:
                    if self.SymbolChecker(content[indices[0]][indices[1]]):
                        #Valid part number
                        #For debugging: valid = "True"
                        sum += int(pn.groups()[0])
                        break
            lineNu += 1

        print("Output is " + str(sum))
        return(sum)    

if __name__ == "__main__":
    partNumbChecker = PartNumChecker()
    partNumbChecker.run()
