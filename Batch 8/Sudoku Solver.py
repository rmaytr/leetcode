from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        LeetCode #37 - Sudoku Solver (Hard)

        Approach — backtracking with constraint sets:
            Precompute three sets of already-placed digits:
              • rows[r]  : digits in row r
              • cols[c]  : digits in column c
              • boxes[b] : digits in 3×3 box b  (b = (r//3)*3 + c//3)

            Collect all empty cells upfront. Fill them recursively: for each
            candidate '1'–'9', skip if it violates any constraint set, place
            it, update all three sets, and recurse to the next empty cell.
            Undo on failure (backtrack). Return True immediately on success.

        Time Complexity:  O(9^E) where E = number of empty cells (≤ 81) —
                          each empty cell has at most 9 candidates. In
                          practice, constraint pruning makes this very fast.
        Space Complexity: O(E) — recursion depth + three sets of size ≤ 9.
        """
        rows: List[set] = [set() for _ in range(9)]
        cols: List[set] = [set() for _ in range(9)]
        boxes: List[set] = [set() for _ in range(9)]
        empty: List[tuple] = []

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == ".":
                    empty.append((r, c))
                else:
                    b = (r // 3) * 3 + c // 3
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

        def backtrack(idx: int) -> bool:
            if idx == len(empty):
                return True
            r, c = empty[idx]
            b = (r // 3) * 3 + c // 3
            for d in "123456789":
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)
                if backtrack(idx + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)
            return False

        backtrack(0)


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    board = [
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
    sol.solveSudoku(board)
    expected = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    assert board == expected

    # Test 2: Validate solution — each row, col, box contains digits 1-9
    digits = set("123456789")
    for r in range(9):
        assert set(board[r]) == digits, f"Row {r} invalid"
    for c in range(9):
        assert {board[r][c] for r in range(9)} == digits, f"Col {c} invalid"
    for br in range(3):
        for bc in range(3):
            box = {board[br*3+dr][bc*3+dc] for dr in range(3) for dc in range(3)}
            assert box == digits, f"Box ({br},{bc}) invalid"

    print("All test cases passed.")
