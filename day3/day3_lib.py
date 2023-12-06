""" Lib providing basic APIs """
from curses.ascii import isxdigit
from enum import IntEnum
from os.path import dirname, join

InputFileList = [
    "./input_sample_1.txt",
    "./input_sample_2.txt",
    "./input.txt",
]

class Position():
    """ Class to locate a char in 2D array """
    x: int
    y: int

    def __init__( self, x=0, y=0 ):
        self.x = x
        self.y = y

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

    def find_surrounding_indices(self, pos, max_pos, corner=False ):
        """ Find possible indices in a 2D matrix """
        index_list = []
        #For strings not in corner, just check up and below
        if not corner:
            if pos.x != 0:
                index_list.append( [pos.x-1,pos.y] )
            if pos.x != max_pos.x-1:
                index_list.append( [pos.x+1,pos.y] )
            return index_list

        # If corner need to deduce 8 adjacent elements
        if pos.x != 0: # Ignore -1 row, if first row
            if pos.y != 0:
                index_list.append( [pos.x-1, pos.y-1] )
            index_list.append( [pos.x-1, pos.y] )
            if pos.y != max_pos.y-1:
                index_list.append( [pos.x-1, pos.y+1] )

        if pos.y != 0:
            index_list.append( [pos.x, pos.y-1] )
        if pos.y != max_pos.y-1:
            index_list.append( [pos.x, pos.y+1] )

        if pos.x != max_pos.x-1: # Ignore +1 row, if last row
            if pos.y != 0:
                index_list.append( [pos.x+1, pos.y-1] )
            index_list.append( [pos.x+1, pos.y] )
            if pos.y != max_pos.y-1 :
                index_list.append( [pos.x+1, pos.y+1] )
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
