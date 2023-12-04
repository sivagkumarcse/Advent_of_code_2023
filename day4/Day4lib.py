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

class PointCard():
    cardNumber = 0
    WinningList = []
    ScratchList = []
    successfulScratch = 0
    count = 0

    def __init__(self, index, WinningList, ScratchList) -> None:
        self.cardNumber = index
        self.WinningList = WinningList
        self.ScratchList = ScratchList
        pass

class Day4lib():
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
    
    def convertStringListToNumberList(self, list):
        temp = 0
        intList = []
        for i in list:
            if i == ' ':
                if temp == 0:
                    continue
                else:
                    intList.append(temp)
                    temp = 0
            else:
                temp = temp*10 + int(i)
        
        if( temp ):
            intList.append(temp)

        return (intList)