""" Lib providing basic APIs """
import re
from enum import IntEnum
from os.path import dirname, join
from itertools import cycle

InputFileList = [
    "./input_sample_1.txt",
    "./input_sample_2.txt",
    "./input_sample_3.txt",
    "./input.txt",
]

class InputLoc(IntEnum):
    """ Enum to select input file """
    SAMPLE_INPUT_1 = 0
    SAMPLE_INPUT_2 = 1
    SAMPLE_INPUT_3 = 2
    ORIGINAL_INPUT = 3

class Day8lib():
    """ Base class for Day 8 puzzle """
    max_row = 0
    max_column = 0

    def __init__( self ):
        self.input_steps = None
        self.maps_network = {}

    def read_file_content( self, input_type ):
        """ Open input file and return its content """
        current_dir = dirname( __file__ )
        input_file_path = join( current_dir, InputFileList[input_type] )

        with open(input_file_path, "r+", encoding="utf8") as input_file:
            lines = input_file.readlines()
        input_file.close()

        self.max_row = len(lines)
        self.max_column = len(lines[0]) - 1
        return lines

    def convert_steps(self, step):
        """ Convert input L|R to 0|1 """
        if step == 'L':
            return 0
        if step == 'R':
            return 1
        return None

    def parse_input_to_maps_network(self, file_content):
        """ Generate input dict and steps from the file content """
        steps_logged = False

        for line in file_content:
            # Read first line which has steps
            if steps_logged is False:
                self.input_steps = [ self.convert_steps(steps) for steps in line if steps != '\n' ]
                steps_logged = True
                continue

            if len(line) != 1: # Ignore line with only '\n'
                re_match = re.findall(r'(\w+)', line)
                self.maps_network[re_match[0]] = [re_match[1], re_match[2]]

    def count_steps(self, current_loc, dest_wildcard=False):
        """ Count steps from current_loc to dest """
        steps = 0
        for direction in cycle(self.input_steps):
            if dest_wildcard is True:
                if current_loc[-1] == 'Z':
                    break
            else:
                if current_loc == 'ZZZ':
                    break
            steps += 1
            current_loc = self.maps_network[current_loc][direction]
        return steps
