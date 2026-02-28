from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        LeetCode #746 - Min Cost Climbing Stairs (Easy)

        Approach — 1D DP with O(1) rolling variables:
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]) — the cheapest total cost
            paid when leaving stair i (stepping on it then jumping off). Base
            cases: dp[0] = cost[0], dp[1] = cost[1]. The answer is
            min(dp[n-1], dp[n-2]) because we can reach the top from either of
            the last two stairs.
            Two rolling variables replace the full array.

        Time Complexity:  O(n).
        Space Complexity: O(1).
        """
        n = len(cost)
        if n == 1:
            return cost[0]
        a, b = cost[0], cost[1]
        for i in range(2, n):
            a, b = b, cost[i] + min(a, b)
        return min(a, b)


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — start at index 1, jump to top: cost 15
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15

    # Test 2: LeetCode example 2 — optimal path avoids the 100-cost stairs
    assert sol.minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ) == 6

    # Test 3: Two stairs — take the cheaper one
    assert sol.minCostClimbingStairs([5, 3]) == 3

    # Test 4: Equal costs
    assert sol.minCostClimbingStairs([4, 4]) == 4

    # Test 5: Long flat array — every step costs 1; pay for every other stair
    assert sol.minCostClimbingStairs([1] * 10) == 5

    print("All test cases passed.")
