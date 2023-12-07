""" Solution to Advent of Code, 2023 - Day 7 Puzzle 1 """
#!/usr/bin/python3
import functools
from day7_lib import Day7lib, InputLoc

class CamelCardScorerJoker(Day7lib):
    """ class for solution to puzzle 1 """
    total_winning = 0
    def run(self):
        """ run method """
        self.main()

    def main(self):
        """ main method """
        # Use SAMPLE_INPUT_2 or ORIGINAL_INPUT
        rank = 1
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)
        self.populate_hand_details(content, joker=True)

        for hand_type in sorted(self.hands.items()):
            hand_type[1].sort( key=functools.cmp_to_key(self.card_compare_with_joker) )
            # After sorting just mulitply bid with rank
            for hand in hand_type[1]:
                self.total_winning += hand.bid * rank
                rank += 1

        print ( f"total_winning is {self.total_winning}" )

if __name__ == "__main__":
    camel_card_scorer_joker = CamelCardScorerJoker()
    camel_card_scorer_joker.run()
