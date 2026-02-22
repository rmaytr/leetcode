import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        LeetCode #1046 - Last Stone Weight (Easy)

        Approach — max-heap simulation:
            Python's heapq is a min-heap, so negate all values to simulate a
            max-heap. Each round, pop the two heaviest stones, smash them, and
            push the remainder (if any) back until at most one stone remains.

        Time Complexity:  O(n log n) — up to n rounds, each heap op is O(log n).
        Space Complexity: O(n) — heap storage.
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, -(a - b))
        return -heap[0] if heap else 0


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

    # Test 2: Single stone
    assert sol.lastStoneWeight([1]) == 1

    # Test 3: Two equal stones — result is 0
    assert sol.lastStoneWeight([3, 3]) == 0

    # Test 4: All same — every pair cancels
    assert sol.lastStoneWeight([5, 5, 5, 5]) == 0

    # Test 5: Two different stones — remainder is the difference
    assert sol.lastStoneWeight([10, 4]) == 6

    print("All test cases passed.")
