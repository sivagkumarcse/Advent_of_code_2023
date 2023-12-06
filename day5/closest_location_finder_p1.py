""" Solution to Advent of Code, 2023 - Day 5 Puzzle 1 """
#!/usr/bin/python3
import re
from day5_lib import Day5lib, InputLoc

class ClosestLocationFinder(Day5lib):
    """ class for solution to puzzle 1 """

    seed2soil = []
    soil2fert = []
    fert2watr = []
    watr2lght = []
    lght2temp = []
    temp2humd = []
    humd2loct = []
    inputSeeds = []

    inputArray = [inputSeeds, seed2soil, soil2fert, fert2watr, watr2lght,
                  lght2temp, temp2humd, humd2loct]

    def __init__(self):
        pass

    def run(self):
        """ run method """
        self.main()

    def check_loc_needed(self, loc, table_index):
        """ check min location to sow the seed """
        #print(loc, table_index)
        if table_index == 1:
            if loc in self.inputArray[table_index-1]:
                print(f"Selected seed is {loc}")
                return True
            return False

        # if not seed to soil table, recursively call again
        table = self.inputArray[table_index-1]
        providedmap = False
        for entry in table:
            if loc in range(entry[0], entry[0] + entry[2]):
                loc_index = loc - entry[0]
                providedmap = True
                nextkey = entry[1] + loc_index
                break

        if providedmap is False:
            nextkey = loc

        return self.check_loc_needed(nextkey, table_index-1)

    def main(self):
        """ main method """
        # Use SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)
        arr_ind = -1
        for line in content:
            match = re.findall(r'([\d]+)', line)
            if "seeds:" in line:
                arr_ind += 1
                match = list(map(int, match))
                self.inputArray[arr_ind] = match

            elif "map:" in line:
                arr_ind += 1

            elif (len(match) != 0 and arr_ind!= -1 ):
                #Convert text input to int list
                match = list(map(int, match))
                self.inputArray[arr_ind].append(match)

        # Find possible location max
        max_loc = 0
        for loc_array in self.humd2loct:
            max_loc = max( max_loc, (loc_array[0] + loc_array[2] - 1) )
            max_loc = max( max_loc, (loc_array[1] + loc_array[2] - 1) )

        # Do reverse search from location 1 to max_loc
        table_len = len(self.inputArray)
        for location in range(0, max_loc+1):
            detected = self.check_loc_needed(location, table_len)
            if detected:
                print(f"Min Location is {location}")
                break

if __name__ == "__main__":
    closestLocationFinder = ClosestLocationFinder()
    closestLocationFinder.run()
