class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] in [".", ","]:
                    continue
                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in cols[col]:
                    return False
                boxid = (row // 3) * 3 + col // 3
                if board[row][col] in boxes[int(boxid)]:
                    return False
                rows[row].append(board[row][col])
                cols[col].append(board[row][col])
                boxes[int(boxid)].append(board[row][col])
        return True