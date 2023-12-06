""" Solution to Advent of Code, 2023 - Day 4 Puzzle 1 """
#!/usr/bin/python3
import re
from day4_lib import Day4lib, InputLoc

class PointCalculator(Day4lib):
    """ class for solution to puzzle 1 """
    pc_pattern = None
    final_score = 0

    def __init__(self):
        self.pc_pattern = re.compile( r'Card +(\d+?):((?: +(\d+))*) \|((?: (\d+| \d))*)' )

    def run(self):
        """ run method """
        self.main()

    def main(self):
        """ main method """
        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day4lib.read_file_content( self, InputLoc.ORIGINAL_INPUT )

        for line in content:
            line_score_multiplier = 0
            match = re.findall(self.pc_pattern, line)
            if match is not None and len(match) != 0:
                winning_list = match[0][1]
                scratch_list = match[0][3]

                winning_list = self.convert_stringlist_to_numberlist(winning_list)
                scratch_list = self.convert_stringlist_to_numberlist(scratch_list)

                for i in scratch_list:
                    if i in winning_list:
                        line_score_multiplier += 1
                        continue

                if line_score_multiplier:
                    self.final_score += pow( 2, line_score_multiplier-1 )

        print( f"final_score is {self.final_score}" )
        return self.final_score


if __name__ == "__main__":
    pointCalculator = PointCalculator()
    pointCalculator.run()
   