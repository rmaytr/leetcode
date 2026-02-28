from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        LeetCode #207 - Course Schedule (Medium)

        Approach — Kahn's algorithm (BFS topological sort):
            Build an adjacency list and an in-degree array from prerequisites.
            Enqueue all courses with in-degree 0 (no prerequisites). Process
            the queue: decrement each successor's in-degree; enqueue any that
            reach 0. If every course is processed (count == numCourses),
            the dependency graph is acyclic → all courses can be finished.

        Time Complexity:  O(V + E) where V = numCourses, E = |prerequisites|.
        Space Complexity: O(V + E) — adjacency list and queue.
        """
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        in_degree: List[int] = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        queue: deque[int] = deque(
            c for c in range(numCourses) if in_degree[c] == 0
        )
        processed = 0

        while queue:
            course = queue.popleft()
            processed += 1
            for nxt in adj[course]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        return processed == numCourses


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — acyclic, can finish
    assert sol.canFinish(2, [[1, 0]]) is True

    # Test 2: LeetCode example 2 — cycle, cannot finish
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False

    # Test 3: No prerequisites — all courses independent
    assert sol.canFinish(5, []) is True

    # Test 4: Linear chain — acyclic
    assert sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]) is True

    # Test 5: Longer cycle involving 4 nodes
    assert sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [0, 3]]) is False

    print("All test cases passed.")
