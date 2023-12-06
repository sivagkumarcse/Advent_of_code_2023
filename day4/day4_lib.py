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

class PointCard():
    """ Base class for Day 4 puzzle """
    card_number = 0
    winning_list = []
    scratch_list = []
    successfulScratch = 0
    count = 0

    def __init__(self, index, winning_list, scratch_list) -> None:
        self.card_number = index
        self.winning_list = winning_list
        self.scratch_list = scratch_list

class Day4lib():
    """ Base class for Day 4 puzzle """
    def __init__( self ):
        pass

    def read_file_content( self, input_type ):
        """ Open input file and return its content """
        current_dir = dirname( __file__ )
        input_file_path = join( current_dir, InputFileList[input_type] )

        with open(input_file_path, "r+", encoding="utf8") as input_file:
            lines = input_file.readlines()
        input_file.close()
        return lines

    def convert_stringlist_to_numberlist(self, str_list):
        """Convert string list into number"""
        temp = 0
        int_list = []
        for i in str_list:
            if i == ' ':
                if temp == 0:
                    continue
                int_list.append(temp)
                temp = 0
            else:
                temp = temp*10 + int(i)

        if temp :
            int_list.append(temp)

        return int_list
    