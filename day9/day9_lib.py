""" Lib providing basic APIs """
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

class Day9lib():
    """ Base class for Day 6 puzzle """
    max_row = 0
    max_column = 0

    def __init__( self ):
        pass

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

    def next_value_predict(self, int_list, history=False):
        next_list = []
        local_return = True

        for i in range (0, len(int_list) - 1):
            next_list.append(int_list[ i+1 ] - int_list[ i ])
            if (next_list[ i ] != 0 and local_return):
                local_return = False

        if (local_return):
            return int_list[ 0 ]
        
        next_val_iter = self.next_value_predict(next_list, history)
        if history:
            int_list.append( int_list[0] - next_val_iter )
        else:
            int_list.append( int_list[-1] + next_val_iter )

        return(int_list[-1])
