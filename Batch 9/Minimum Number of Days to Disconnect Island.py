import sys
from typing import List

sys.setrecursionlimit(10_000)


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """
        LeetCode #1568 - Minimum Number of Days to Disconnect Island (Hard)

        Approach — observation + articulation-point detection:
            The answer is always 0, 1, or 2:
              0 days: grid already has ≠ 1 island.
              1 day:  (a) exactly 1 land cell exists (removing it → 0 islands),
                      (b) some land cell is an articulation point — removing it
                          splits the island into ≥ 2 components.
              2 days: always sufficient; removing two strategically chosen cells
                      can isolate any land corner.

            Algorithm:
              1. Count islands and total land cells; return 0 if ≠ 1 island.
              2. Return 1 if land == 1.
              3. Run Tarjan's articulation-point DFS on the land graph.
                 Return 1 if any AP found, else 2.

        Time Complexity:  O(M × N) — island count + single AP-detection DFS.
        Space Complexity: O(M × N) — disc/low arrays and recursion stack.
        """
        rows, cols = len(grid), len(grid[0])

        def count_islands() -> tuple[int, int]:
            """Returns (number of islands, total land cells). Uses iterative DFS."""
            visited = [[False] * cols for _ in range(rows)]
            islands = land = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        land += 1
                    if grid[r][c] == 1 and not visited[r][c]:
                        islands += 1
                        stack = [(r, c)]
                        while stack:
                            cr, cc = stack.pop()
                            if visited[cr][cc]:
                                continue
                            visited[cr][cc] = True
                            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                                nr, nc = cr + dr, cc + dc
                                if (0 <= nr < rows and 0 <= nc < cols
                                        and grid[nr][nc] == 1
                                        and not visited[nr][nc]):
                                    stack.append((nr, nc))
            return islands, land

        islands, land = count_islands()
        if islands != 1:
            return 0
        if land == 1:
            return 1

        # Tarjan's articulation-point detection on the land subgraph
        disc: list[list[int]] = [[-1] * cols for _ in range(rows)]
        low: list[list[int]] = [[0] * cols for _ in range(rows)]
        timer = [0]
        has_ap = [False]

        def dfs_ap(r: int, c: int, pr: int, pc: int) -> None:
            disc[r][c] = low[r][c] = timer[0]
            timer[0] += 1
            children = 0
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    if disc[nr][nc] == -1:
                        children += 1
                        dfs_ap(nr, nc, r, c)
                        low[r][c] = min(low[r][c], low[nr][nc])
                        # Root AP: ≥2 DFS-tree children
                        if pr == -1 and children > 1:
                            has_ap[0] = True
                        # Non-root AP: child subtree cannot reach above current node
                        if pr != -1 and low[nr][nc] >= disc[r][c]:
                            has_ap[0] = True
                    elif (nr, nc) != (pr, pc):
                        low[r][c] = min(low[r][c], disc[nr][nc])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs_ap(r, c, -1, -1)
                    break
            else:
                continue
            break

        return 1 if has_ap[0] else 2


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — single 2×2 island, no AP, needs 2 days
    grid1 = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    assert sol.minDays([row[:] for row in grid1]) == 2

    # Test 2: LeetCode example 2 — cell (1,2) is an AP linking left and right, 1 day
    grid2 = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
    ]
    assert sol.minDays([row[:] for row in grid2]) == 1

    # Test 3: Single land cell → remove it → 0 islands, 1 day
    grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert sol.minDays([row[:] for row in grid3]) == 1

    # Test 4: Already 2 separate islands → 0 days
    grid4 = [[1, 0, 1]]
    assert sol.minDays([row[:] for row in grid4]) == 0

    # Test 5: 2×2 all land — no AP, 2 days needed
    grid5 = [[1, 1], [1, 1]]
    assert sol.minDays([row[:] for row in grid5]) == 2

    print("All test cases passed.")
