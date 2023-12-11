""" Lib providing basic APIs """
import itertools
from enum import IntEnum
from os.path import dirname, join

InputFileList = [
    "./input_sample_1.txt",
    "./input_sample_2.txt",
    "./input.txt",
]

class InputLoc(IntEnum):
    """ Enum to select input file """
    SAMPLE_INPUT_1 = 0
    SAMPLE_INPUT_2 = 1
    ORIGINAL_INPUT = 2

class Galaxy():
    """ Maintains position of a galaxy """
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Day11lib():
    """ Base class for Day 11 puzzle """
    max_row = 0
    max_column = 0
    content = []
    galaxies = []

    def __init__( self ):
        pass

    def read_file_content( self, input_type ):
        """ Open input file and return its content """
        current_dir = dirname( __file__ )
        input_file_path = join( current_dir, InputFileList[input_type] )

        with open(input_file_path, "r+", encoding="utf8") as input_file:
            lines = input_file.readlines()
        input_file.close()

        for line in lines:
            self.content.append(list(line.strip()))

        self.max_row = len(lines)
        self.max_column = len(lines[0]) - 1

    def find_galaxies(self):
        """ Find location of galaxy in the universe """
        for x_index, row in enumerate(self.content):
            galaxy_columns = [i for i, x in enumerate(row) if x == '#']
            for y_index in galaxy_columns:
                self.galaxies.append(Galaxy(x_index,y_index))

    def expand_universe(self):
        """ Expand the input file for empty spaces """
        column_galaxy_finder = []
        row_empty_list = []
        for row_index,row in enumerate(self.content):
            if row.count('.') == self.max_column:
                row_empty_list.append(row_index)
            else:
                galaxy_columns = [i for i, x in enumerate(row) if x == '#']
                column_galaxy_finder += galaxy_columns

        for i in sorted(row_empty_list, reverse=True):
            new_row = []
            new_row[:] = itertools.repeat('X', self.max_column)
            self.content.insert(i, new_row)
            self.max_row += 1

        for row_index,row in enumerate(self.content):
            for c in reversed(range(0, self.max_column)):
                if c not in column_galaxy_finder:
                    row.insert(c, 'X')

        # Update galaxy location after expanded
        self.find_galaxies()


    def compute_min_path(self,first_galaxy, second_galaxy, mutlipler=2):
        """ Return distance between two galaxies """
        count_of_expanded_space = 0
        min_x = min(first_galaxy.x, second_galaxy.x)
        max_x = max(first_galaxy.x, second_galaxy.x)
        min_y = min(first_galaxy.y, second_galaxy.y)
        max_y = max(first_galaxy.y, second_galaxy.y)

        x_dist = max_x - min_x
        y_dist = max_y - min_y

        for x_index in range (min_x, max_x):
            if self.content[x_index][0] == 'X':
                count_of_expanded_space += 1
                x_dist -= 1

        for y_index in range (min_y, max_y):
            if self.content[0][y_index] == 'X':
                count_of_expanded_space += 1
                y_dist -= 1
        return x_dist + y_dist + (count_of_expanded_space*(mutlipler-1))
