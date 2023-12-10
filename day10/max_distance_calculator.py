""" Puzzle 1 """
#!/usr/bin/python3
from day10_lib import Day10lib
from day10_lib import InputLoc
from day10_lib import Position

class MaxDistanceCalculator(Day10lib):
    """ Puzzle 1 solution """
    def run(self):
        """ Run method """
        self.main()

    def main(self):
        """ Main method """
        # Use either SAMPLE_INPUT_1 or SAMPLE_INPUT_2 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)
        for index,line in enumerate(content):
            if 'S' in line:
                starting_index = Position(index, line.index('S'))

        branch_index = self.next_step_index(starting_index, multiple=True)
        max_distance = 1

        while branch_index[0].is_different(branch_index[1]):
            max_distance += 1
            branch_index[0] = self.next_step_index(branch_index[0])
            branch_index[1] = self.next_step_index(branch_index[1])
        print (f"Maximum distance from start of loop is {max_distance}")

if __name__ == "__main__":
    max_distance_calculator = MaxDistanceCalculator()
    max_distance_calculator.run()
