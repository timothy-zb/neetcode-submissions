
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                item = board[i][j]

                # Ignore empty cells
                if item == ".":
                    continue

                # Calculate which 3x3 box
                box = (i // 3) * 3 + (j // 3)

                # Check duplicates
                if (item in rows[i] or
                    item in cols[j] or
                    item in boxes[box]):
                    return False

                # Add number to respective sets
                rows[i].add(item)
                cols[j].add(item)
                boxes[box].add(item)

        return True
