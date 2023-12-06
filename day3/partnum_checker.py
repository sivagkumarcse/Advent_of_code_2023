""" Solution to Advent of Code, 2023 - Day 3 Puzzle 1 """
#!/usr/bin/python3
import re
from day3_lib import Day3Lib, InputLoc

PNpattern = re.compile( r'(\d+)' )

class PartNumChecker(Day3Lib):
    """ class for solution to puzzle 1 """
    def run(self):
        """ run method """
        self.main()

    # Main implementation
    def main(self):
        """ main method """
        final_sum = 0
        line_nu = 0

        # SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = Day3Lib.read_file_content(self, InputLoc.ORIGINAL_INPUT)

        # For every line
        for line in content:
            # For every Part number in a line
            for pn in PNpattern.finditer( line ):
                index_list = []
                index_list_temp = []

                for i in range( pn.span()[0], pn.span()[1] ):
                    if ( i == pn.span()[0] ) or \
                       ( i == pn.span()[1] - 1):
                        corner = True
                    else:
                        corner = False
                    index_list.extend( self.find_surrounding_indices
                                      ( line_nu, i,
                                        self.max_row,
                                        self.max_column,
                                        corner=corner ) )

                # Remove duplicate indices to check
                for item in index_list:
                    if item not in index_list_temp:
                        index_list_temp.append(item)
                index_list = index_list_temp
                index_list_temp = None

                # Check if special character is surrounding the part number
                for indices in index_list:
                    if self.symbol_checker(content[indices[0]][indices[1]]):
                        #Valid part number
                        #For debugging: valid = "True"
                        final_sum += int(pn.groups()[0])
                        break
            line_nu += 1

        print("Output is " + str(final_sum))
        return final_sum

if __name__ == "__main__":
    partNumbChecker = PartNumChecker()
    partNumbChecker.run()