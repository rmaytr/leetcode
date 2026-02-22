import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        LeetCode #215 - Kth Largest Element in an Array (Medium)

        Approach — min-heap of size k:
            Stream through nums maintaining a min-heap of at most k elements.
            When the heap exceeds k, pop the smallest — so the heap always
            holds the k largest values seen so far. After processing all
            numbers, the heap root is the k-th largest element.

            Alternative: heapq.nlargest(k, nums)[-1] is concise but builds
            the full heap internally. Quickselect gives O(n) average but
            O(n²) worst case without median-of-medians.

        Time Complexity:  O(n log k) — each push/pop is O(log k).
        Space Complexity: O(k) — heap is bounded to k elements.
        """
        heap: List[int] = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — 2nd largest in [1,2,3,4,5,6]
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    # Test 2: LeetCode example 2
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    # Test 3: k == len — return minimum
    assert sol.findKthLargest([1, 2, 3], 3) == 1

    # Test 4: Single element
    assert sol.findKthLargest([7], 1) == 7

    # Test 5: Duplicates
    assert sol.findKthLargest([5, 5, 5, 5], 2) == 5

    print("All test cases passed.")
