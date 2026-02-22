import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        LeetCode #973 - K Closest Points to Origin (Medium)

        Approach — max-heap of size k:
            Maintain a max-heap (distances negated for Python's min-heap) of
            the k closest points seen so far. For each new point, push it; if
            the heap grows beyond k, pop the farthest point. The root always
            holds the k-th closest candidate, acting as an admission threshold.

            Squared distances are used throughout to avoid sqrt overhead and
            maintain integer arithmetic.

        Time Complexity:  O(n log k) — each push/pop is O(log k).
        Space Complexity: O(k) — heap bounded to k entries.
        """
        heap: list = []  # (-dist_sq, x, y)
        for x, y in points:
            dist_sq = x * x + y * y
            heapq.heappush(heap, (-dist_sq, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — [-2,2] is closer (dist²=8) than [1,3] (dist²=10)
    assert sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]

    # Test 2: LeetCode example 2 — closest 2 of 3 points
    result = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(result) == sorted([[3, 3], [-2, 4]])

    # Test 3: k == len — return all points
    points = [[1, 1], [2, 2]]
    assert sorted(sol.kClosest(points, 2)) == sorted(points)

    # Test 4: Origin included — it is trivially closest
    result = sol.kClosest([[0, 0], [1, 1]], 1)
    assert result == [[0, 0]]

    # Test 5: Negative coordinates
    result = sol.kClosest([[-1, -1], [3, 4]], 1)
    assert result == [[-1, -1]]  # dist²=2 vs 25

    print("All test cases passed.")
