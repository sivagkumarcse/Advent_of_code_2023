""" Puzzle 1 """
#!/usr/bin/python3
from itertools import groupby
from day13_lib import Day13lib
from day13_lib import InputLoc

class MirrorFinderWithSmudge(Day13lib):
    """ Puzzle 1 solution """
    def __init__(self):
        pass

    def run(self):
        """ Run method """
        self.main()

    def row_diff(self, pattern, r_first, r_next):
        """ For row in comparison, return different element count """
        row_first = pattern[r_first]
        row_next = pattern[r_next]
        count = 0

        for ele1,ele2 in zip(row_first, row_next):
            if ele1 == ele2:
                count +=1
        return len(row_first) - count

    def row_mirror_check_with_smudge(self, pattern, start, row_len, smudge):
        """ Find row index which is the mirror """
        smudge_allowed = smudge
        multiply  = start * 2 - 1
        for split in range (start, row_len):
            mirror = multiply - split
            diff = self.row_diff(pattern, mirror, split)
            if diff > 1:
                return False
            if diff == 1:
                if smudge_allowed >= 1:
                    smudge_allowed -= 1
                else:
                    return False
            if mirror == 0:
                if smudge_allowed:
                    return False
                return True
            continue
        if smudge_allowed:
            return False
        return True

    def col_diff(self, pattern, c_first, c_next):
        """ For column in comparison, return different element count """
        count = 0
        rows_count =0
        for row in pattern:
            rows_count += 1
            if row[c_first] == row[c_next]:
                count += 1
        return rows_count - count

    def column_mirror_check_with_smudge(self, pattern, start, col_len, smudge):
        """ Find column index which is the mirror """
        smudge_allowed = smudge
        multiply  = start * 2 - 1
        for split in range (start, col_len):
            mirror = multiply - split
            diff =  self.col_diff(pattern, mirror, split)
            if diff > 1:
                return False
            if diff == 1:
                if smudge_allowed >= 1:
                    smudge_allowed -= 1
                else:
                    return False
            if mirror == 0:
                if smudge_allowed:
                    return False
                return True
            continue
        if smudge_allowed:
            return False
        return True

    def find_summarizing_pattern(self, patterns, smudge=0):
        """ Solution to puzzle 1 and puzzle 2 """
        hor_count = 0
        ver_count = 0

        for pattern in patterns:
            row_len = len(pattern)
            col_len = len(pattern[0])
            hor_found = False

            # Split in row
            for start_index in range(1, row_len):
                if self.row_mirror_check_with_smudge(pattern, start_index, row_len, smudge):
                    hor_count += start_index
                    hor_found = True
                    break

            if hor_found is False:
                for start_index in range(1, col_len):
                    if self.column_mirror_check_with_smudge(pattern, start_index, col_len, smudge):
                        ver_count += start_index
                        break
        return hor_count*100 + ver_count

    def main(self):
        """ Main method """
        patterns = []
        sol1 = sol2 = 0
        # Input can be SAMPLE_INPUT_1 or ORIGINAL_INPUT or SAMPLE_INPUT_2
        self.read_file_content(InputLoc.ORIGINAL_INPUT)
        patterns = [list(pattern) for ele, pattern in groupby(self.content, key = bool) if ele]
        sol1 = self.find_summarizing_pattern(patterns)
        sol2 = self.find_summarizing_pattern(patterns, smudge=1)
        print(f"Solution 1 : Summarizing note is {sol1}")
        print(f"Solution 2 : Summarizing note is {sol2}")

if __name__ == "__main__":
    mirrorFinderWithSmudge = MirrorFinderWithSmudge()
    mirrorFinderWithSmudge.run()
