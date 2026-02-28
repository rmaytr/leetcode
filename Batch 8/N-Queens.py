from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        LeetCode #51 - N-Queens (Hard)

        Approach — row-by-row backtracking with O(1) conflict sets:
            Place exactly one queen per row. Track three sets:
              • cols  : columns already occupied by a queen.
              • diag1 : left diagonals (r − c is constant along each).
              • diag2 : right diagonals (r + c is constant along each).
            For each column in the current row, skip it if any set is hit.
            On a full placement (row == n), build the board string and record
            it. Undo all set insertions when backtracking.

        Time Complexity:  O(n!) — at most n! placements explored; building
                          each board string costs O(n²).
        Space Complexity: O(n) — three sets + queen-column array.
        """
        result: List[List[str]] = []
        cols: set[int] = set()
        diag1: set[int] = set()   # r - c
        diag2: set[int] = set()   # r + c
        queens: List[int] = [-1] * n  # queens[row] = column placed

        def backtrack(row: int) -> None:
            if row == n:
                board = [
                    "." * queens[r] + "Q" + "." * (n - queens[r] - 1)
                    for r in range(n)
                ]
                result.append(board)
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens[row] = col
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: n=4 — exactly 2 solutions
    result = sol.solveNQueens(4)
    assert len(result) == 2
    assert sorted(result) == sorted([
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ])

    # Test 2: n=1 — trivially one solution
    assert sol.solveNQueens(1) == [["Q"]]

    # Test 3: n=8 — 92 distinct solutions
    assert len(sol.solveNQueens(8)) == 92

    # Test 4: Verify board structure — each row has exactly one 'Q'
    for board in sol.solveNQueens(5):
        assert len(board) == 5
        assert all(row.count("Q") == 1 for row in board)

    print("All test cases passed.")
