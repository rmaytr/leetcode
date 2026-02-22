import heapq


class MedianFinder:
    """
    LeetCode #295 - Find Median from Data Stream (Hard)

    Approach — two heaps (max-heap lower half, min-heap upper half):
        Partition all numbers into two halves:
          • lo: max-heap of the smaller half (values stored negated).
          • hi: min-heap of the larger half.

        Invariant maintained after every addNum:
          - Every element in lo ≤ every element in hi.
          - |len(lo) - len(hi)| ≤ 1, with lo allowed one extra element.

        To preserve the ordering invariant, always push the incoming value
        through hi first (so the true maximum of lo goes to hi), then pull
        back from hi if hi grows larger than lo. This two-step dance ensures
        the max of lo never exceeds the min of hi.

        findMedian is O(1): peek lo for odd total; average the two tops for even.

    Time Complexity:  O(log n) per addNum; O(1) per findMedian.
    Space Complexity: O(n) — all n elements reside in the two heaps.
    """

    def __init__(self) -> None:
        self.lo: list[int] = []  # max-heap (values negated)
        self.hi: list[int] = []  # min-heap

    def addNum(self, num: int) -> None:
        # Push to lo, then push lo's max to hi to preserve ordering invariant.
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Rebalance: lo may hold at most one more element than hi.
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1: LeetCode example
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    # Test 2: Single element
    mf2 = MedianFinder()
    mf2.addNum(5)
    assert mf2.findMedian() == 5.0

    # Test 3: Even count — average of two middle elements
    mf3 = MedianFinder()
    for n in [6, 1, 3, 4]:
        mf3.addNum(n)
    assert mf3.findMedian() == 3.5  # sorted: [1,3,4,6] → (3+4)/2

    # Test 4: Negative numbers
    mf4 = MedianFinder()
    mf4.addNum(-1)
    mf4.addNum(-2)
    assert mf4.findMedian() == -1.5  # sorted: [-2,-1] → (-2+-1)/2

    # Test 5: Duplicates
    mf5 = MedianFinder()
    mf5.addNum(2)
    mf5.addNum(2)
    assert mf5.findMedian() == 2.0

    print("All test cases passed.")
