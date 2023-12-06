""" Solution to Advent of Code, 2023 - Day 4 Puzzle 2 """
#!/usr/bin/python3
import re
from day4_lib import Day4lib, InputLoc, PointCard

class PointCalculator(Day4lib):
    """ class for solution to puzzle 2 """
    pc_pattern = None
    final_score = 0
    point_cards = []

    def __init__(self):
        self.pc_pattern = re.compile( r'Card +(\d+?):((?: +(\d+))*) \|((?: (\d+| \d))*)' )
        point_card = PointCard(0, None, None)
        # Dummy point card with index 0
        self.point_cards.append(point_card)

    def run(self):
        """ run method """
        self.main()

    def main(self):
        """ main method """
        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day4lib.read_file_content( self, InputLoc.ORIGINAL_INPUT )

        # Generate Card DB
        for line in content:
            match = re.findall(self.pc_pattern, line)
            if match is not None and len(match) != 0:
                winning_list = match[0][1]
                scratch_list = match[0][3]
                card_number = match[0][0]
                winning_list = self.convert_stringlist_to_numberlist(winning_list)
                scratch_list = self.convert_stringlist_to_numberlist(scratch_list)

                # Create a point_card with provided number
                point_card = PointCard(card_number, winning_list, scratch_list)
                self.point_cards.append(point_card)
                point_card.count = 1

                for i in scratch_list:
                    if i in winning_list:
                        point_card.successfulScratch += 1

        # Process scratches
        for card in self.point_cards:
            cur_card_number = int(card.card_number)
            end_card_number = cur_card_number + (card.successfulScratch)
            for next_card_index in range(cur_card_number + 1, end_card_number + 1):
                self.point_cards[next_card_index].count += card.count

        # Calculate total cards
        for card in self.point_cards:
            self.final_score += card.count

        print( f"final_score is {self.final_score}" )
        return self.final_score


if __name__ == "__main__":
    pointCalculator = PointCalculator()
    pointCalculator.run()
   