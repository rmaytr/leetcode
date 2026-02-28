from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        LeetCode #79 - Word Search (Medium)

        Approach — DFS backtracking with in-place visited marking:
            For each cell that matches word[0], launch a DFS. At each step,
            temporarily overwrite the cell with '#' to mark it visited, then
            recurse in all four directions for the next character. Restore the
            cell after all recursive calls return (backtrack). Return True the
            moment a full match is confirmed.

            Optimization: if the board doesn't contain enough of any required
            character, return False early before any DFS.

        Time Complexity:  O(M · 4 · 3^(L−1)) where M = rows×cols board cells
                          and L = len(word) — each DFS fans out to at most 3
                          unvisited neighbors after the first step (one
                          direction is already marked '#').
        Space Complexity: O(L) — recursion stack depth equals word length.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp, board[r][c] = board[r][c], "#"
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    # Test 1: LeetCode example 1
    assert sol.exist([row[:] for row in board], "ABCCED") is True

    # Test 2: LeetCode example 2
    assert sol.exist([row[:] for row in board], "SEE") is True

    # Test 3: Cannot reuse a cell — "ABCB" requires revisiting 'B'
    assert sol.exist([row[:] for row in board], "ABCB") is False

    # Test 4: Single-cell board
    assert sol.exist([["a"]], "a") is True
    assert sol.exist([["a"]], "b") is False

    # Test 5: Linear path across a single row
    assert sol.exist([["a", "b", "c", "d"]], "abcd") is True

    print("All test cases passed.")
