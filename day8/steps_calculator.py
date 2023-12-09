""" Puzzle 1 """
#!/usr/bin/python3
import sys
from math import lcm
from day8_lib import Day8lib
from day8_lib import InputLoc

class StepsCalculator(Day8lib):
    """ Puzzle 1 solution """
    sum_of_prediction = 0

    def run(self):
        """ Run method """
        self.main()

    def main(self):
        """ Main method """
        sys.setrecursionlimit(25000)
        ghost_total_steps = []
        total_steps = 0
        total_steps_p2 = 1 # For LCM calculation
        # Use either SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)
        self.parse_input_to_maps_network(content)

        try:
            total_steps = self.count_steps("AAA")
        except KeyError:
            print("Unsupported input file for puzzle 1")
            total_steps = 0

        print( f"Solution 1: Total steps to reach from AAA->ZZZ is {total_steps}" )

        for key in self.maps_network:
            if 'A' == key[-1]:
                ghost_total_steps.append(self.count_steps(key, dest_wildcard=True) )
        try:
            for step in ghost_total_steps:
                total_steps_p2 = lcm(step, total_steps_p2)
        except KeyError:
            print("Unsupported input file for puzzle 1")
            total_steps_p2 = 0

        print( f"Solution 2: Total steps to reach from ..A->..Z is {total_steps_p2}" )
        return total_steps, total_steps_p2

if __name__ == "__main__":
    stepsCalculator = StepsCalculator()
    stepsCalculator.run()
