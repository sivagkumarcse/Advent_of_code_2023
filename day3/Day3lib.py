from curses.ascii import isxdigit
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

class Day3lib():
    maxRow = 0
    maxColumn = 0

    def __init__( self ):
        self.maxRow = 0
        self.maxColumn = 0

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
    
    def findSurroundingIndices(self, x, y, maxX=0, maxY=0, corner=False ):
        indexList = []
        #For strings not in corner, just check up and below
        if not corner:
            if( x != 0 ):
                indexList.append( [x-1,y] )
            if( x != maxX-1 ):
                indexList.append( [x+1,y] )    
            return(indexList)

        # If corner need to deduce 8 adjacent elements    
        if( x != 0 ): # Ignore -1 row, if first row
            if( y != 0 ):
                indexList.append( [x-1, y-1] )
            indexList.append( [x-1, y] )
            if( y != maxY-1 ):
                indexList.append( [x-1, y+1] )

        if( y != 0 ):
            indexList.append( [x, y-1] )
        if( y != maxY-1 ):
            indexList.append( [x, y+1] )

        if( x != maxX-1 ): # Ignore +1 row, if last row
            if( y != 0 ):
                indexList.append( [x+1, y-1] )
            indexList.append( [x+1, y] )
            if( y != maxY-1 ):
                indexList.append( [x+1, y+1] )
        return(indexList)
    
    def SymbolChecker( self, character ):
        if (character == '.' or isxdigit(character) ):
            return False
        else:
            return True
        
    def GearChecker( self, character ):
        if (character == '*' ):
            return True
        else:
            return False
