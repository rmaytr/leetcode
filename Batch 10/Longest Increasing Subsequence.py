import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        LeetCode #300 - Longest Increasing Subsequence (Medium)

        Approach — patience sorting with binary search:
            Maintain a `tails` array where tails[i] is the smallest possible
            tail value of any increasing subsequence of length i+1 seen so far.
            For each number:
              • If it is greater than all tails, extend by appending.
              • Otherwise, replace the leftmost tail value ≥ num with num
                (binary search with bisect_left — strictly increasing, so we
                replace the first tail that is ≥ num).
            The length of `tails` at the end equals the LIS length.
            (tails itself is not necessarily a valid subsequence, but its
            length is correct.)

        Time Complexity:  O(n log n) — binary search per element.
        Space Complexity: O(n) — tails array.
        """
        tails: List[int] = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — LIS is [2,3,7,101] or others, length 4
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    # Test 2: LeetCode example 2 — LIS is [0,1,2,3], length 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4

    # Test 3: LeetCode example 3 — all equal, LIS length 1
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1

    # Test 4: Already sorted — entire array is LIS
    assert sol.lengthOfLIS([1, 2, 3, 4, 5]) == 5

    # Test 5: Reverse sorted — every element is its own LIS
    assert sol.lengthOfLIS([5, 4, 3, 2, 1]) == 1

    print("All test cases passed.")
