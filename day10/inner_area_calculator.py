""" Puzzle 2 """
#!/usr/bin/python3
import itertools
from day10_lib import Day10lib
from day10_lib import InputLoc
from day10_lib import Position

class InnerAreaCalculator(Day10lib):
    """ Puzzle 2 solution """

    # Class variable
    array_2d = None
    loop_indices = None
    outer_indices = None

    def __init__(self):
        super().__init__()
        self.array_2d = []
        self.loop_indices = []
        self.outer_indices = []

    def run(self):
        """ Run method """
        self.main()

    def main(self):
        """ Main method """
        # Use any input file
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)
        for index,line in enumerate(content):
            self.array_2d.append(list(line.strip()))
            if 'S' in line:
                starting_index = Position(index, line.index('S'))

        self.loop_indices.append([starting_index.x,starting_index.y])
        next_index = self.next_step_index(starting_index)
        while next_index.is_different(starting_index):
            self.loop_indices.append([next_index.x,next_index.y])
            next_index = self.next_step_index(next_index)
            if next_index is None:
                break

        for row_index,line in enumerate(self.array_2d):
            for column_index in range (len(line)):
                if [row_index, column_index] in self.loop_indices:
                    self.array_2d[row_index][column_index] = 'L'
                else:
                    self.array_2d[row_index][column_index] = '0'

        print (f"Area of inner loop is {self.print_bigger_maze()}")

    def print_bigger_maze(self):
        """ Interesting solution from r/user/EViLeleven/ """
        bigger_maze_visual = []#self.max_row*3]
        for _ in itertools.repeat(None, 3*(self.max_row+1)):
            line = []
            for _ in itertools.repeat(None, 3*(self.max_column+1)):
                line.append('1')
            bigger_maze_visual.append(line)

        for i, line in enumerate(self.content):
            for j, char in enumerate(line):
                if [i, j] not in self.loop_indices:
                    bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                    bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '0'
                    bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                    bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '0'
                    bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '0'
                    bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '0'
                    bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                    bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '0'
                    bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'
                else:
                    if char == 'S':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = "+"
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = "+"
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = "+"
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = "+"
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = "+"
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = "+"
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = "+"
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = "+"
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = "+"
                    if char ==  '-':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'
                    if char ==  '|':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'
                    if char ==  'J':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'
                    if char ==   '7':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'
                    if char ==  'F':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'
                    if char ==  'L':
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] = '0'
                        bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] = '0'
                        bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] = '#'
                        bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] = '0'

        bigger_maze_visual = self.t2_eleminate_outer_area(bigger_maze_visual)

        answer2 = 0
        for i, line in enumerate(self.content):
            for j, char in enumerate(line):
                if bigger_maze_visual[(i * 3) + 0][(j * 3) + 0] == "0" and \
                   bigger_maze_visual[(i * 3) + 1][(j * 3) + 0] == "0" and \
                   bigger_maze_visual[(i * 3) + 2][(j * 3) + 0] == "0" and \
                   bigger_maze_visual[(i * 3) + 0][(j * 3) + 1] == "0" and \
                   bigger_maze_visual[(i * 3) + 1][(j * 3) + 1] == "0" and \
                   bigger_maze_visual[(i * 3) + 2][(j * 3) + 1] == "0" and \
                   bigger_maze_visual[(i * 3) + 0][(j * 3) + 2] == "0" and \
                   bigger_maze_visual[(i * 3) + 1][(j * 3) + 2] == "0" and \
                   bigger_maze_visual[(i * 3) + 2][(j * 3) + 2] == "0":
                    answer2 += 1

        return answer2

    def t2_find_untouched_area(self, bigger_maze_visual):
        """ Find count of elements with value '0' """
        area = 0
        for row in bigger_maze_visual:
            area += row.count('0')
        return area

    def t2_eleminate_outer_area(self, bigger_maze_visual):
        """ Set 1 for elements in outer area """
        inital_area = self.t2_find_untouched_area(bigger_maze_visual)
        print(f"Initial area is {inital_area}")
        for row_index,row in enumerate(bigger_maze_visual):
            for column_index in range(0, len(row)):
                if bigger_maze_visual[row_index][column_index] not in ['#','+','1']:
                    if row_index in [0, (self.max_row*3-1)] or\
                       column_index in [0,(3*self.max_column-1)]:
                        bigger_maze_visual[row_index][column_index] = '1'
                    elif bigger_maze_visual[row_index-1][column_index] == '1' or \
                         bigger_maze_visual[row_index+1][column_index] == '1' or \
                         bigger_maze_visual[row_index][column_index-1] == '1' or \
                         bigger_maze_visual[row_index][column_index+1] == '1':
                        bigger_maze_visual[row_index][column_index] = '1'

        modified_area = self.t2_find_untouched_area(bigger_maze_visual)
        print(f"Modified area is {modified_area}")

        # Exit condition of recurssion
        if inital_area == modified_area:
            return bigger_maze_visual
        return self.t2_eleminate_outer_area(bigger_maze_visual)

if __name__ == "__main__":
    innerAreaCalculator = InnerAreaCalculator()
    innerAreaCalculator.run()
