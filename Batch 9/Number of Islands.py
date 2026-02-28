import sys
from typing import List

sys.setrecursionlimit(100_000)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        LeetCode #200 - Number of Islands (Medium)

        Approach — DFS flood-fill (in-place marking):
            For each unvisited land cell ('1'), increment the island counter
            and launch a DFS that sinks all connected land by overwriting '1'
            with '0'. This marks the entire island as visited in one pass
            without a separate visited array.

        Time Complexity:  O(M × N) — each cell visited at most once.
        Space Complexity: O(M × N) — recursion stack depth in the worst case
                          (all land, one giant snake-shaped island).
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"  # sink visited land
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — 3 separate islands
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert sol.numIslands([row[:] for row in grid1]) == 3

    # Test 2: LeetCode example 2 — all land forms 1 island
    grid2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert sol.numIslands([row[:] for row in grid2]) == 1

    # Test 3: All water → 0 islands
    assert sol.numIslands([["0", "0"], ["0", "0"]]) == 0

    # Test 4: All land → 1 island
    assert sol.numIslands([["1", "1"], ["1", "1"]]) == 1

    # Test 5: Single cell
    assert sol.numIslands([["1"]]) == 1
    assert sol.numIslands([["0"]]) == 0

    print("All test cases passed.")
