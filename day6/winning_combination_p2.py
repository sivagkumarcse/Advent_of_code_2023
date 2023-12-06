""" Puzzle 1 """
#!/usr/bin/python3
import re
from day6_lib import Day6lib
from day6_lib import InputLoc

class WinningCombination(Day6lib):
    """ Puzzle 1 solution """
    solution = 0

    def __init__(self):
        pass

    def run(self):
        """ Run method """
        self.main()

    def find_winning_combination(self, time, dist):
        """" Do math to find the winning combination """
        lcombination = 0

        # Solution is a bell curve, fails at range 0th millisecond to
        # lcombination and then passes for a range, then failure happens
        # again in range lcombination to last millisecond
        for combination in range (0, time):
            if combination * (time-combination) < dist:
                lcombination+=1
            else:
                break
        # Result include time: last milli second, but not 0th.
        # Hence add 1
        return time - lcombination*2 + 1

    def main(self):
        """ Main method """
        # Use either SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)

        # Read inputs from file
        input_time_arr = re.findall(r'([\d]+)', content[0])
        time = int( ''.join(input_time_arr) )
        input_dist_arr = re.findall(r'([\d]+)', content[1])
        dist = int( ''.join(input_dist_arr) )

        solution = self.find_winning_combination( time, dist )

        print( f"Winning combinatios multiplier is {solution}" )

if __name__ == "__main__":
    winningCombination = WinningCombination()
    winningCombination.run()
