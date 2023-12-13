""" Puzzle 1 and 2 """
#!/usr/bin/python3
from day11_lib import Day11lib
from day11_lib import InputLoc

class MinPathFinder(Day11lib):
    """ Puzzle 1 and 2 solution """
    min_path_list = []

    def __init__(self):
        pass

    def run(self):
        """ Run method """
        self.main()

    def main(self):
        """ Main method """
        sum_of_min_path = 0

        self.read_file_content(InputLoc.ORIGINAL_INPUT)
        self.expand_universe()

        for galaxy_index, first_galaxy in enumerate(self.galaxies):
            for second_galaxy in self.galaxies[galaxy_index+1:]:
                sum_of_min_path += self.compute_min_path(first_galaxy, second_galaxy)

        print(f"Solution 1 : Sum of minpath between galaxies is {sum_of_min_path}")

        sum_of_min_path = 0
        for galaxy_index, first_galaxy in enumerate(self.galaxies):
            for second_galaxy in self.galaxies[galaxy_index+1:]:
                sum_of_min_path += self.compute_min_path(first_galaxy, second_galaxy, \
                                                         mutlipler=1000000)
        print(f"Solution 2 : Sum of minpath between galaxies is {sum_of_min_path}")

if __name__ == "__main__":
    minPathFinder = MinPathFinder()
    minPathFinder.run()
