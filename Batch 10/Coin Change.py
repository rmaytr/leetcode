from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        LeetCode #322 - Coin Change (Medium)

        Approach — bottom-up 1D DP (unbounded knapsack):
            dp[i] = minimum number of coins needed to make amount i.
            dp[0] = 0 (base); dp[i] = min(dp[i - c] + 1) for each coin c ≤ i.
            Initialize all other entries to amount + 1 (sentinel for
            "unreachable"), so any reachable amount will produce a smaller
            value after the coin updates.

        Time Complexity:  O(amount × len(coins)).
        Space Complexity: O(amount).
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] <= amount else -1


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — 11 = 5+5+1, 3 coins
    assert sol.coinChange([1, 2, 5], 11) == 3

    # Test 2: LeetCode example 2 — amount unreachable
    assert sol.coinChange([2], 3) == -1

    # Test 3: Amount 0 — always 0 coins needed
    assert sol.coinChange([1], 0) == 0

    # Test 4: Single large coin equals amount
    assert sol.coinChange([7], 7) == 1

    # Test 5: Greedy fails — optimal is 3×4=12 not 10+1+1
    assert sol.coinChange([1, 3, 4, 5], 7) == 2  # 3+4

    print("All test cases passed.")
