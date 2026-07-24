class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            seen = set()
            for n in row:
                if n == ".":
                    continue
                elif n in seen:
                    return False
                elif n not in seen:
                    seen.add(n)
        
        # check columns
        for pos in range(9):
            seen = set()
            for row in range(9):
                if board[row][pos] == ".":
                    continue
                elif board[row][pos] in seen:
                    return False
                elif board[row][pos] not in seen:
                    seen.add(board[row][pos])
                
        #check blocks
        for r in range(0, 9, 3):
            for c in range(0,9,3):
                seen = set()
                for row in range(r,r+3):
                    for col in range(c,c+3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] in seen:
                            return False
                        elif board[row][col] not in seen:
                            seen.add(board[row][col])
        return True
