from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        LeetCode #417 - Pacific Atlantic Water Flow (Medium)

        Approach — reverse multi-source BFS from each ocean border:
            Water flows from high to low (or equal height). Reversing the
            direction: starting from ocean borders, BFS uphill (neighbor
            height ≥ current) to find all cells that can drain to that ocean.
            Pacific borders: top row and left column.
            Atlantic borders: bottom row and right column.
            Cells reachable from both sets form the answer.

        Time Complexity:  O(M × N) — each cell visited at most twice (once per BFS).
        Space Complexity: O(M × N) — visited sets and BFS queues.
        """
        rows, cols = len(heights), len(heights[0])

        def bfs(starts: list[tuple[int, int]]) -> set[tuple[int, int]]:
            visited: set[tuple[int, int]] = set(starts)
            queue: deque[tuple[int, int]] = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific_starts = (
            [(0, c) for c in range(cols)] +
            [(r, 0) for r in range(1, rows)]
        )
        atlantic_starts = (
            [(rows - 1, c) for c in range(cols)] +
            [(r, cols - 1) for r in range(rows - 1)]
        )

        return [
            [r, c]
            for r, c in bfs(pacific_starts) & bfs(atlantic_starts)
        ]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    result1 = sorted(map(tuple, sol.pacificAtlantic(heights1)))
    expected1 = sorted([(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)])
    assert result1 == expected1

    # Test 2: 1×1 grid — single cell drains to both oceans
    assert sol.pacificAtlantic([[1]]) == [[0, 0]]

    # Test 3: Flat grid — every cell reaches both oceans
    heights3 = [[1, 1], [1, 1]]
    result3 = sorted(map(tuple, sol.pacificAtlantic(heights3)))
    assert result3 == sorted([(0, 0), (0, 1), (1, 0), (1, 1)])

    # Test 4: Single row — borders are both ocean cells; middle must flow outward
    heights4 = [[1, 2, 1]]
    result4 = sorted(map(tuple, sol.pacificAtlantic(heights4)))
    assert (0, 0) in result4 and (0, 2) in result4

    print("All test cases passed.")
