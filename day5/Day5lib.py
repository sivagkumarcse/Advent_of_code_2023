from enum import IntEnum
from os.path import dirname, join

# class syntax

InputFileList = [
    "./input_sample_1.txt",
    "./input_sample_2.txt",
    "./input.txt",
]

class INPUT_LOC(IntEnum):
    SAMPLE_INPUT_1 = 0
    SAMPLE_INPUT_2 = 1
    ORIGINAL_INPUT = 2

class Day5lib():
    def __init__( self ):
        pass

    def readFileContent( self, inputType ):
        CurrentDir = dirname( __file__ )
        InputFilePath = join( CurrentDir, InputFileList[inputType] )

        try:
            inputFile = open( InputFilePath, "r+" )
        except Exception:
            print( "Error: File does not appear to exist." )
            return None
        
        lines = inputFile.readlines()
        inputFile.close()
        self.maxRow = len(lines)
        self.maxColumn = len(lines[0]) - 1 
        return (lines)