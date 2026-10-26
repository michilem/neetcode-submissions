class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        for r in range(len(board)):
            row = set()
            for c in range(len(board)):
                v = board[r][c]
                if v == ".":
                    continue
                if v not in row:
                    row.add(v)
                else:
                    return False

                if v not in cols[c]:
                    cols[c].add(v)
                else:
                    return False

                if v not in boxes[3 * (r // 3) + c // 3]:
                    boxes[3 * (r // 3) + c // 3].add(v)
                else:
                    return False
        return True