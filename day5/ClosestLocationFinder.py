#!/usr/bin/python3
from Day5lib import *

class ClosestLocationFinder(Day5lib):
    def __init__(self):
        pass
    
    def run(self):
        self.main()

    def main(self):
        # Use SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.readFileContent(INPUT_LOC.SAMPLE_INPUT_1)
        print(content)

if __name__ == "__main__":
    closestLocationFinder = ClosestLocationFinder()
    closestLocationFinder.run()