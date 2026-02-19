from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        LeetCode #36 - Valid Sudoku (Medium)

        Approach:
            Single pass over all 81 cells. For each filled cell (value != '.'),
            check three sets simultaneously:
              - rows[r]  : digits seen in row r
              - cols[c]  : digits seen in column c
              - boxes[b] : digits seen in 3×3 box b  (b = (r//3)*3 + c//3)
            If a digit already exists in any of these sets, the board is
            invalid. Otherwise, add it to all three and continue.

        Time Complexity:  O(1) — the board is always 9×9 = 81 cells.
        Space Complexity: O(1) — sets are bounded by 9 digits × 27 groups.
        """
        rows: dict[int, set] = defaultdict(set)
        cols: dict[int, set] = defaultdict(set)
        boxes: dict[int, set] = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_id = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid board from LeetCode
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(valid_board) is True

    # Test 2: Invalid board — duplicate '8' in top-left box
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(invalid_board) is False

    print("All test cases passed.")
