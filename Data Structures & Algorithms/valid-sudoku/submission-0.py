class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9x9 sudoku board
        # sudoku board valid if
        # each ropw contains digits 1-9 (no duplicates)
        # each col contains digits 1-9
        # eeach box contains 1=9
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        row_num = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] != '.':
                    box = (i // 3) * 3 + (j // 3)
                    if board[i][j] not in cols[i]:
                        cols[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in rows[j]:
                        rows[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in boxes[box]:
                        boxes[box].add(board[i][j])
                    else:
                        return False
        return True