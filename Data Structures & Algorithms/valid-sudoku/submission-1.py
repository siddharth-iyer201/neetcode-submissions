class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            rowValuesSeen = set()
            for col in range(cols):
                if board[row][col] != '.':
                    if int(board[row][col]) in rowValuesSeen:
                        return False
                    rowValuesSeen.add(int(board[row][col]))
                startRow = row // 3 * 3
                startCol = col // 3 * 3
                squareValuesSeen = set()
                for r in range(startRow, startRow + 3):
                    for c in range(startCol, startCol + 3):
                        if board[r][c] != ".":
                            if int(board[r][c]) in squareValuesSeen:
                                return False
                            squareValuesSeen.add(int(board[r][c]))
        for col in range(cols):
            colValuesSeen = set()
            for row in range(rows):
                if board[row][col] != '.':
                    if int(board[row][col]) in colValuesSeen:
                        return False
                    colValuesSeen.add(int(board[row][col]))
        return True
                    
