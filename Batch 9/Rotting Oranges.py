from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        LeetCode #994 - Rotting Oranges (Medium)

        Approach — multi-source BFS from all initially rotten oranges:
            Seed the BFS queue with every rotten orange (value 2) at minute 0
            and count fresh oranges (value 1). Each BFS level represents one
            minute: spread rot to all fresh 4-connected neighbors, decrement
            the fresh counter, and advance the minute count. After BFS, any
            remaining fresh orange is unreachable → return -1; otherwise
            return elapsed minutes (0 if no fresh oranges existed).

        Time Complexity:  O(M × N) — each cell enqueued and processed at most once.
        Space Complexity: O(M × N) — BFS queue in the worst case.
        """
        rows, cols = len(grid), len(grid[0])
        queue: deque[tuple[int, int]] = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — 4 minutes to rot all
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert sol.orangesRotting([row[:] for row in grid1]) == 4

    # Test 2: LeetCode example 2 — isolated fresh orange, impossible
    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert sol.orangesRotting([row[:] for row in grid2]) == -1

    # Test 3: No fresh oranges — already done, 0 minutes
    assert sol.orangesRotting([[0, 2]]) == 0

    # Test 4: Single fresh orange adjacent to rotten — 1 minute
    assert sol.orangesRotting([[2, 1]]) == 1

    # Test 5: All fresh, no rotten — impossible
    assert sol.orangesRotting([[1, 1], [1, 1]]) == -1

    print("All test cases passed.")
