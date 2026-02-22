import heapq
from typing import List


class KthLargest:
    """
    LeetCode #703 - Kth Largest Element in a Stream (Easy)

    Approach — min-heap of size k:
        Maintain a min-heap that holds exactly the k largest elements seen so
        far. The heap root (minimum of the heap) is always the k-th largest.
        On each add: push the new value, then pop the smallest if size > k.

    Time Complexity:  O(log k) per add call; O(n log k) for construction.
    Space Complexity: O(k) — heap never exceeds k elements.
    """

    def __init__(self, k: int, nums: List[int]) -> None:
        self.k = k
        self.heap: List[int] = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1: LeetCode example
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8

    # Test 2: k=1 — always return the running maximum
    kth2 = KthLargest(1, [])
    assert kth2.add(3) == 3
    assert kth2.add(1) == 3
    assert kth2.add(5) == 5

    # Test 3: k equals initial stream size
    kth3 = KthLargest(2, [1, 2])
    assert kth3.add(0) == 1   # top-2 are {1,2}, 2nd largest = 1

    print("All test cases passed.")
