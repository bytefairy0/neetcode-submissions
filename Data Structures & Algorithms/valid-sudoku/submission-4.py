class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for each row and colums
        for rowIdx in range(9):
            rowHash = {}
            colHash = {}
            for colIdx in range(9):
                rowElement = board[rowIdx][colIdx]
                colElement = board[colIdx][rowIdx]
                if rowElement in rowHash or colElement in colHash:
                    print("rowIdx, colIdx: ", rowIdx, colIdx)
                    return False
                if rowElement != '.':
                    rowHash[rowElement] = 1
                if colElement != '.':
                    colHash[colElement] = 1

        # check for each Grid
        for gridNum in range(9):
            gridHash = {}
            # its 3x3 grid - flatten each grid
            # for each grid
            rs = int(gridNum / 3)*3
            cs = (gridNum*3) % 9
            for r in range(rs, rs+3):
                for c in range(cs, cs+3):
                    element = board[r][c]
                    if element in gridHash:
                        return False
                    if element != '.':
                        gridHash[element] = 1

        return True
                
            
        