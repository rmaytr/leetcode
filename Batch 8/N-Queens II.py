class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        LeetCode #52 - N-Queens II (Hard)

        Approach — backtracking with bitmask conflict tracking:
            Represent occupied columns and diagonals as integer bitmasks of
            width n rather than sets, giving O(1) conflict detection via
            bitwise OR and a single AND to compute available columns.

            At each row, `available` is the set of free columns:
                available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

            Iterate available columns by repeatedly isolating the lowest set
            bit (bit = available & -available) and clearing it. When row == n,
            all n queens are placed — increment the count.

            Diagonal shifts: moving from row r to r+1, a left-diagonal (r−c
            constant) attack shifts one column RIGHT → shift left-diagonal
            mask LEFT; a right-diagonal (r+c constant) attack shifts one
            column LEFT → shift right-diagonal mask RIGHT.

        Time Complexity:  O(n!) — same search space as N-Queens; bitmasks
                          reduce constant factors vs set-based approach.
        Space Complexity: O(n) — recursion depth only.
        """
        self._count = 0
        full = (1 << n) - 1  # mask with n LSBs set

        def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
            if row == n:
                self._count += 1
                return
            available = full & ~(cols | diag1 | diag2)
            while available:
                bit = available & (-available)   # isolate lowest set bit
                available &= available - 1       # clear lowest set bit
                backtrack(
                    row + 1,
                    cols | bit,
                    (diag1 | bit) << 1,
                    (diag2 | bit) >> 1,
                )

        backtrack(0, 0, 0, 0)
        return self._count


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: n=1 — one solution
    assert sol.totalNQueens(1) == 1

    # Test 2: n=4 — two solutions
    assert sol.totalNQueens(4) == 2

    # Test 3: n=8 — 92 solutions (classical result)
    assert sol.totalNQueens(8) == 92

    # Test 4: n=6 — 4 solutions
    assert sol.totalNQueens(6) == 4

    # Test 5: n=9 — 352 solutions
    assert sol.totalNQueens(9) == 352

    print("All test cases passed.")
