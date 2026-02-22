from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        LeetCode #875 - Koko Eating Bananas (Medium)

        Approach:
            Binary search on the answer. The eating speed k lies in [1, max(piles)].
            For a given speed k, the hours needed is sum(ceil(pile / k)) for all
            piles. This function is monotonically non-increasing in k, so binary
            search finds the smallest k where hours_needed <= h. Use
            math.ceil(pile / k) — equivalent to (pile + k - 1) // k — to avoid
            floating-point issues.

        Time Complexity:  O(n log m) — n = len(piles), m = max(piles); binary
                          search runs O(log m) iterations, each scanning all n piles.
        Space Complexity: O(1) — only scalar variables.
        """
        def hours_needed(speed: int) -> int:
            return sum(math.ceil(pile / speed) for pile in piles)

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if hours_needed(mid) <= h:
                right = mid          # mid is feasible; try slower
            else:
                left = mid + 1       # too slow; must go faster
        return left


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4

    # Test 2: Plenty of time — minimum speed of 1 works
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

    # Test 3: Exactly enough hours
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    # Test 4: Single pile
    assert sol.minEatingSpeed([10], 3) == 4

    # Test 5: Speed equals max pile size (h == len(piles))
    assert sol.minEatingSpeed([1, 1, 1, 999999999], 4) == 999999999

    print("All test cases passed.")
