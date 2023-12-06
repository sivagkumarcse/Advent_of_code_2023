""" Lib providing basic APIs """
from curses.ascii import isxdigit
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

class Day3Lib():
    """ Base class for Day 3 puzzle """
    max_row = 0
    max_column = 0

    def __init__( self ):
        self.max_row = 0
        self.max_column = 0

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

    def find_surrounding_indices(self, x, y, max_x=0, max_y=0, corner=False ):
        """ Find possible indices in a 2D matrix """
        index_list = []
        #For strings not in corner, just check up and below
        if not corner:
            if x != 0:
                index_list.append( [x-1,y] )
            if x != max_x-1:
                index_list.append( [x+1,y] )
            return index_list

        # If corner need to deduce 8 adjacent elements
        if x != 0: # Ignore -1 row, if first row
            if y != 0:
                index_list.append( [x-1, y-1] )
            index_list.append( [x-1, y] )
            if y != max_y-1:
                index_list.append( [x-1, y+1] )

        if y != 0:
            index_list.append( [x, y-1] )
        if y != max_y-1:
            index_list.append( [x, y+1] )

        if x != max_x-1: # Ignore +1 row, if last row
            if y != 0:
                index_list.append( [x+1, y-1] )
            index_list.append( [x+1, y] )
            if y != max_y-1 :
                index_list.append( [x+1, y+1] )
        return index_list

    def symbol_checker( self, character ):
        """ Check if the charcter is a symbol """
        if (character == '.' or isxdigit(character) ):
            return False
        return True

    def gear_checker( self, character ):
        """ Check if the charcter is a gear (*) """
        if character == '*':
            return True
        return False
