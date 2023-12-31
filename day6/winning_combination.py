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
        wcombination = 0

        for combination in range (0, time):
            if combination * (time-combination) > dist:
                wcombination+=1
        return wcombination

    def main(self):
        """ Main method """
        solution = None

        # Use either SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)

        # Read inputs from file
        input_time_arr = list( map (int, re.findall(r'([\d]+)', content[0]) ))
        input_dist_arr = list( map (int, re.findall(r'([\d]+)', content[1]) ))

        for (time, dist) in zip( input_time_arr, input_dist_arr ):
            if solution:
                solution *= self.find_winning_combination( time, dist )
            else:
                solution = self.find_winning_combination( time, dist )

        print( f"Winning combinatios multiplier is {solution}" )

if __name__ == "__main__":
    winningCombination = WinningCombination()
    winningCombination.run()
