#!/usr/bin/python3
from Day4lib import *
import re

class PointCalculator(Day4lib):
    PCpattern = None
    finalScore = 0

    def __init__(self):
        self.PCpattern = re.compile( r'Card +(\d+?):((?: +(\d+))*) \|((?: (\d+| \d))*)' )
        pass
    
    def run(self):
        self.main()

    # Main implementation
    def main(self):
        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day4lib.readFileContent( self, INPUT_LOC.ORIGINAL_INPUT )
        if not content:
            return(0)
        
        for line in content:
            lineScoreMultiplier = 0
            match = re.findall(self.PCpattern, line)
            if match is not None and len(match) != 0:
                winningList = match[0][1]
                scratchList = match[0][3]

                winningList = self.convertStringListToNumberList(winningList)
                scratchList = self.convertStringListToNumberList(scratchList)

                for i in scratchList:
                    if i in winningList:
                        lineScoreMultiplier += 1
                        continue
                
                if( lineScoreMultiplier ):
                    self.finalScore += pow( 2, lineScoreMultiplier-1 )
    
        print(f"FinalScore is {self.finalScore}")
        return(self.finalScore)


if __name__ == "__main__":
    pointCalculator = PointCalculator()
    pointCalculator.run()
   