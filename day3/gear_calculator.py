""" Solution to Advent of Code, 2023 - Day 3 Puzzle 2 """
#!/usr/bin/python3
import re
from day3_lib import Day3Lib, InputLoc, Position

class GearCalulator(Day3Lib):
    """ class for solution to puzzle 2 """
    PNpattern = re.compile( r'(\d+)' )
    GearPair = {}
    max_pos = None

    def run(self):
        """ run method"""
        self.main()

    def main(self):
        """ main method """
        line_nu = 0
        sum_gear_ratio = 0
        pos = Position()

        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day3Lib.read_file_content(self, InputLoc.ORIGINAL_INPUT)
        self.max_pos = Position(self.max_row, self.max_column)

       # For every line
        for line in content:
            # For every Part number in a line
            for pn in self.PNpattern.finditer( line ):
                index_list = []
                index_list_temp = []

                for i in range( pn.span()[0], pn.span()[1] ):
                    # Check if index is first or last character
                    corner = (i in (pn.span()[0], pn.span()[1] - 1))
                    pos.x = line_nu
                    pos.y = i
                    index_list.extend( self.find_surrounding_indices
                                      ( pos, self.max_pos, corner=corner ) )

                # Remove duplicate indices to check
                for item in index_list:
                    if item not in index_list_temp:
                        index_list_temp.append(item)
                index_list = index_list_temp
                index_list_temp = None

                # Check if the part number has * surrounding it
                for indices in index_list:
                    if self.gear_checker(content[indices[0]][indices[1]]):

                        # Create a dictonary with index of '*' as key
                        dict_tuple = tuple([indices[0],indices[1]])
                        if dict_tuple in self.GearPair:
                            self.GearPair[dict_tuple].append(int(pn.groups()[0]))
                        else:
                            self.GearPair[dict_tuple] = [int(pn.groups()[0])]
                        break
            line_nu += 1

        # We have the GearPair, multiply and find the value if list size is 2
        for gear_list in self.GearPair.values():
        #    print(key, "->", self.GearPair[key])
            if len(gear_list) == 2:
                sum_gear_ratio += gear_list[0] * gear_list[1]

        print("Output is " + str(sum_gear_ratio))
        return sum_gear_ratio

if __name__ == "__main__":
    gearCalulator = GearCalulator()
    gearCalulator.run()
