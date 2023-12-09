""" Puzzle 1 """
#!/usr/bin/python3
import re
from day8_lib import Day8lib
from day8_lib import InputLoc

class StepsCalculator(Day8lib):
    """ Puzzle 1 solution """
    sum_of_prediction = 0

    def __init__(self):
        pass

    def run(self):
        """ Run method """
        self.main()

    def main(self):
        """ Main method """
        total_steps = 0
        # Use either SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.SAMPLE_INPUT_1)

        print(content)
        print( f"Total steps to reach from AAA->ZZZ is {total_steps}" )
        return total_steps


if __name__ == "__main__":
    stepsCalculator = StepsCalculator()
    stepsCalculator.run()
