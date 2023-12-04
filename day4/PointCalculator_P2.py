#!/usr/bin/python3
from Day4lib import *
import re

class PointCalculator(Day4lib):
    PCpattern = None
    finalScore = 0
    pointCards = []

    def __init__(self):
        self.PCpattern = re.compile( r'Card +(\d+?):((?: +(\d+))*) \|((?: (\d+| \d))*)' )
        pointCard = PointCard(0, None, None)
        # Dummy point card with index 0
        self.pointCards.append(pointCard)
    
    def run(self):
        self.main()

    # Main implementation
    def main(self):
        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day4lib.readFileContent( self, INPUT_LOC.ORIGINAL_INPUT )
        if not content:
            return(0)
        
        # Generate Card DB
        for line in content:
            lineScoreMultiplier = 0
            match = re.findall(self.PCpattern, line)
            if match is not None and len(match) != 0:
                winningList = match[0][1]
                scratchList = match[0][3]
                cardNumber = match[0][0]
                winningList = self.convertStringListToNumberList(winningList)
                scratchList = self.convertStringListToNumberList(scratchList)

                # Create a pointcard with provided number
                pointCard = PointCard(cardNumber, winningList, scratchList)
                self.pointCards.append(pointCard)
                pointCard.count = 1

                for i in scratchList:
                    if i in winningList:
                        pointCard.successfulScratch += 1
                
        # Process scratches
        for card in self.pointCards:
            curCardNumber = int(card.cardNumber)
            endCardNumber = curCardNumber + (card.successfulScratch)
            for nextCardIndex in range(curCardNumber + 1, endCardNumber + 1):
                self.pointCards[nextCardIndex].count += card.count

        # Calculate total cards
        for card in self.pointCards:
            self.finalScore += card.count

        print(f"FinalScore is {self.finalScore}")
        return(self.finalScore)


if __name__ == "__main__":
    pointCalculator = PointCalculator()
    pointCalculator.run()
   