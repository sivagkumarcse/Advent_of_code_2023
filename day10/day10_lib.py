""" Lib providing basic APIs """
from enum import IntEnum
from os.path import dirname, join

InputFileList = [
    "./input.txt",
    "./input_sample_1.txt",
    "./input_sample_2.txt",
    "./input_sample_3.txt",
    "./input_sample_4.txt",
    "./input_sample_5.txt",
    "./input_sample_6.txt",
]

class InputLoc(IntEnum):
    """ Enum to select input file """
    ORIGINAL_INPUT = 0
    SAMPLE_INPUT_1 = 1
    SAMPLE_INPUT_2 = 2
    SAMPLE_INPUT_3 = 3
    SAMPLE_INPUT_4 = 4
    SAMPLE_INPUT_5 = 5
    SAMPLE_INPUT_6 = 6

class Direction(IntEnum):
    """" Enum to represent direction """
    SELF = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Position():
    """ Class to represent a position """
    x = 0
    y = 0
    direction = 0

    def __init__(self, x, y, direction=0):
        self.x = x
        self.y = y
        self.direction = direction

    def is_different(self, compare_index):
        """ Check if position in list are same """
        if self.x == compare_index.x and \
           self.y == compare_index.y:
            return False
        return True

class Day10lib():
    """ Base class for Day 10 puzzle """
    max_row = 0
    max_column = 0
    max_pos = None
    content = None

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
        self.max_pos = Position(self.max_row, self.max_column)
        self.content = lines
        return lines

    def find_surrounding_indices( self, pos, max_pos ):
        """ Find 4 indices in a 2D matrix """
        index_list = []
        # If corner need to deduce 8 adjacent elements
        if pos.x > 0 and pos.direction != Direction.SOUTH:
            index_list.append(Position(pos.x-1, pos.y, Direction.NORTH))
        if pos.x < max_pos.x-1 and pos.direction != Direction.NORTH:
            index_list.append(Position(pos.x+1, pos.y, Direction.SOUTH))

        if pos.y > 0 and pos.direction != Direction.EAST:
            index_list.append(Position(pos.x, pos.y-1, Direction.WEST))
        if pos.y < max_pos.y-1 and pos.direction != Direction.WEST:
            index_list.append(Position(pos.x, pos.y+1,Direction.EAST))


        return index_list

    def next_step_index( self, pos, multiple=False ):
        """ Find next step(s) in loop for given position """
        possible_index = []

        cur_symbol = self.content[pos.x][pos.y]
        surrounding_index = self.find_surrounding_indices(pos, self.max_pos)
        for iter_index in surrounding_index:
            next_symbol = self.content[iter_index.x][iter_index.y]
            next_direction = iter_index.direction

            if self.valid_symbol(cur_symbol, next_symbol, next_direction):
                possible_index.append(iter_index)

            if not multiple and len(possible_index) != 0:
                return possible_index[0]

        if multiple:
            return possible_index
        # Should not be hitting until Start is reached
        return None

    def valid_symbol(self, cur_symbol, next_symbol, next_direction):
        """ Return if next symbol is traversable """
        direction_check = {
            Direction.NORTH:['|', 'F', '7'],
            Direction.EAST: ['-', '7', 'J'],
            Direction.WEST: ['-', 'F', 'L'],
            Direction.SOUTH:  ['|', 'J', 'L'],
            Direction.SELF: []
        }

        next_direction_check = {
            Direction.NORTH:['F', '7','-'],
            Direction.EAST: ['J', '7','|'],
            Direction.WEST: ['L', 'F','|'],
            Direction.SOUTH:['J', 'L','-'],
            Direction.SELF: []
        }
        if next_symbol not in direction_check[next_direction]:
            return False

        if cur_symbol  in next_direction_check[next_direction]:
            return False
        return True
