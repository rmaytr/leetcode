from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        LeetCode #329 - Longest Increasing Path in a Matrix (Hard)

        Approach — DFS with memoization (top-down DP):
            For each cell, the longest increasing path starting from it equals
            1 + max(LIP from each strictly greater 4-connected neighbor).
            Cache computed values to avoid redundant recomputation.

            No explicit visited set is needed: strictly increasing paths cannot
            revisit a cell (a cycle would require equal or decreasing values
            somewhere, contradicting "strictly increasing").

        Time Complexity:  O(M × N) — each cell computed exactly once.
        Space Complexity: O(M × N) — memoization table and recursion stack.
        """
        rows, cols = len(matrix), len(matrix[0])
        memo: dict[tuple[int, int], int] = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            best = 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))
            memo[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — path 1→2→6→9, length 4
    matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert sol.longestIncreasingPath(matrix1) == 4

    # Test 2: LeetCode example 2 — path 3→4→5→6, length 4
    matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    assert sol.longestIncreasingPath(matrix2) == 4

    # Test 3: Single cell → length 1
    assert sol.longestIncreasingPath([[7]]) == 1

    # Test 4: Strictly decreasing row — full row is an increasing path backwards
    assert sol.longestIncreasingPath([[1, 2, 3, 4, 5]]) == 5

    # Test 5: Uniform values — no increasing neighbors, length = 1
    assert sol.longestIncreasingPath([[3, 3], [3, 3]]) == 1

    print("All test cases passed.")
