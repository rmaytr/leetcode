from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        LeetCode #312 - Burst Balloons (Hard)

        Approach — interval DP (think last-to-burst, not first):
            Pad nums with sentinel 1s on both ends so boundary multiplications
            are well-defined. dp[l][r] = maximum coins obtainable by bursting
            every balloon strictly between indices l and r.

            Key insight: instead of choosing which balloon to burst FIRST
            (which splits the problem in a hard-to-track way), choose which
            balloon k to burst LAST within the range (l, r). At that moment,
            its neighbors are nums[l] and nums[r] (the borders), contributing
            nums[l] × nums[k] × nums[r]. The sub-problems dp[l][k] and
            dp[k][r] are then independent.

            Iterate over increasing gap lengths; for each (l, r), try every
            possible last-burst k ∈ (l, r).

        Time Complexity:  O(n³) — three nested loops over n+2 padded elements.
        Space Complexity: O(n²) — DP table.
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):                 # gap = r - l
            for left in range(n - gap):
                right = left + gap
                for k in range(left + 1, right):
                    coins = (dp[left][k]
                             + nums[left] * nums[k] * nums[right]
                             + dp[k][right])
                    if coins > dp[left][right]:
                        dp[left][right] = coins

        return dp[0][n - 1]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — optimal: burst 1→5→3→8, coins = 167
    assert sol.maxCoins([3, 1, 5, 8]) == 167

    # Test 2: LeetCode example 2 — burst order 1→5 or 5→1
    assert sol.maxCoins([1, 5]) == 10

    # Test 3: Single balloon — coins = 1×val×1
    assert sol.maxCoins([5]) == 5

    # Test 4: Two equal balloons
    assert sol.maxCoins([3, 3]) == 12   # burst first 3: 1×3×3=9, then 1×3×1=3 → 12
                                         # or burst second: 1×3×3=9, then 1×3×1=3 → same

    # Test 5: Already verified manual trace for [3,1,5,8]:
    #   burst 1 (→15), burst 5 (→120), burst 3 (→24), burst 8 (→8) = 167
    assert sol.maxCoins([3, 1, 5, 8]) == 167

    print("All test cases passed.")
