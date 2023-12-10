""" Puzzle 2 """
#!/usr/bin/python3
import itertools
from day10_lib import Day10lib
from day10_lib import InputLoc
from day10_lib import Position

class InnerAreaCalculator(Day10lib):
    """ Puzzle 2 solution """

    # Class variable
    loop_indices = None
    bigger_maze = None

    def __init__(self):
        super().__init__()
        self.loop_indices = []
        self.bigger_maze = []


    def run(self):
        """ Run method """
        self.main()

    def initialize_bigger_maze(self):
        """ Initialize a maze 3 times the original input to map
        one element to 9 element. So area outside loop can be
        effectively flooded.
        """
        for _ in itertools.repeat(None, 3*(self.max_row)):
            line = []
            for _ in itertools.repeat(None, 3*(self.max_column)):
                line.append('0')
            self.bigger_maze.append(line)

    def map_loop_to_bigger_maze(self, filler, bit_map, i, j):
        """ Draw a filler for a loop element in bigger maze"""
        for map_iter in range (0, 9):
            i_index = int ( (3 * i) + (map_iter / 3) )
            j_index = int ( (3 * j) + (map_iter % 3) )
            self.bigger_maze[i_index][j_index] = \
                filler if (bit_map>>map_iter & 1) else '0'

    def compute_untouched_inner_area(self):
        """ After flooding find 3x3 0s, which represent the area inside loop """
        answer = 0
        # For every element in origial content, check if its bigger maze 3x3
        # is all 0
        for i, line in enumerate(self.content):
            for j in range(len(line.strip())):
                is_all_zero = True
                for map_iter in range (0, 9):
                    i_index = int ( (3 * i) + (map_iter / 3) )
                    j_index = int ( (3 * j) + (map_iter % 3) )
                    if self.bigger_maze[i_index][j_index] != '0':
                        is_all_zero = False
                        break
                answer += 1 if is_all_zero else 0
        return answer

    def find_untouched_area(self):
        """ Find count of elements with value '0' """
        area = 0
        for row in self.bigger_maze:
            area += row.count('0')
        return area

    def print_bigger_maze(self):
        """ Print bigger maze for debug purpose """
        print("Bigger Maze: \n")
        for line in self.bigger_maze:
            print(*line)

    def eleminate_outer_area(self):
        """ Set 1 for elements in outer area by flooding every recursion """
        inital_area = self.find_untouched_area()
        #print(f"Initial outer area is {inital_area}")
        for row_index,row in enumerate(self.bigger_maze):
            for column_index in range(0, len(row)):
                if self.bigger_maze[row_index][column_index] not in ['#','+','1']:
                    if row_index in [0, (self.max_row*3-1)] or\
                       column_index in [0,(3*self.max_column-1)]:
                        self.bigger_maze[row_index][column_index] = '1'
                    elif self.bigger_maze[row_index-1][column_index] == '1' or \
                         self.bigger_maze[row_index+1][column_index] == '1' or \
                         self.bigger_maze[row_index][column_index-1] == '1' or \
                         self.bigger_maze[row_index][column_index+1] == '1':
                        self.bigger_maze[row_index][column_index] = '1'

        modified_area = self.find_untouched_area()
        #print(f"Modified outer area is {modified_area}")

        # If no improvement from flooding, return
        if inital_area == modified_area:
            return
        self.eleminate_outer_area()

    def area_finder(self):
        """ Interesting solution inspired from r/user/EViLeleven/ """
        self.initialize_bigger_maze()
        for i, line in enumerate(self.content):
            for j, char in enumerate(line.strip()):
                if [i,j] in self.loop_indices:
                    filler = '#'
                    if char == 'S':
                        filler = '+'
                        bit_map = 0x1FF
                    if char == '-':
                        bit_map = 0x38
                    if char ==  '|':
                        bit_map = 0x92
                    if char ==  'J':
                        bit_map = 0x1A
                    if char ==   '7':
                        bit_map = 0x98
                    if char ==  'F':
                        bit_map = 0xB0
                    if char ==  'L':
                        bit_map = 0x32
                    self.map_loop_to_bigger_maze(filler, bit_map, i, j)
        self.eleminate_outer_area()
        return self.compute_untouched_inner_area()

    def main(self):
        """ Main method """
        # Use any input file
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)

        # Loop and make a list of indices of the loop element
        for index,line in enumerate(content):
            if 'S' in line:
                starting_index = Position(index, line.index('S'))
                break
        self.loop_indices.append([starting_index.x,starting_index.y])
        next_index = self.next_step_index(starting_index)
        while next_index.is_different(starting_index):
            self.loop_indices.append([next_index.x,next_index.y])
            next_index = self.next_step_index(next_index)
            if next_index is None:
                break

        print (f"Area of inner loop is {self.area_finder()}")

if __name__ == "__main__":
    innerAreaCalculator = InnerAreaCalculator()
    innerAreaCalculator.run()
