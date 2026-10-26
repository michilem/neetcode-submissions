class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _  in range(9)]
        cols = [set() for _  in range(9)]
        square = dict()
        for r, row in enumerate(board):
            for c, v in enumerate(row):
                if v == '.': continue
                if v in rows[r]: 
                    return False
                else: 
                    rows[r].add(v)

                if v in cols[c]: 
                    return False
                else:
                    cols[c].add(v)

                box_key = (r // 3, c //3)                   
                if box_key not in square:
                    square[box_key] = set()
                if v in square[box_key]:
                    return False
                else:
                    square[box_key].add(v)
        return True