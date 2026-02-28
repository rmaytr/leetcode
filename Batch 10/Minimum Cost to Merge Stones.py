from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
        LeetCode #1000 - Minimum Cost to Merge Stones (Hard)

        Approach — interval DP with prefix sums:
            Observation: merging k piles into 1 reduces the count by k-1.
            Starting from n piles, merging to 1 pile requires (n-1) to be
            divisible by (k-1). If not → return -1.

            dp[i][j] = minimum cost to reduce piles[i..j] to the fewest
            possible groups. For a range of length L, that minimum is
            (L-1) % (k-1) + 1 piles.

            Recurrence: split [i, j] at i, i+(k-1), i+2*(k-1), ...
              • dp[i][m] always reduces [i, m] to exactly 1 pile
                (since (m-i) is a multiple of k-1).
              • Combine: dp[i][j] = min over m of (dp[i][m] + dp[m+1][j]).
              • When (j-i) % (k-1) == 0, the range can collapse to 1 pile —
                pay the range sum (prefix[j+1] - prefix[i]) as the final merge.

        Time Complexity:  O(n³ / k) — three nested loops.
        Space Complexity: O(n²) — DP table.
        """
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i, s in enumerate(stones):
            prefix[i + 1] = prefix[i] + s

        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — k=2 binary merges
    assert sol.mergeStones([3, 2, 4, 1], 2) == 20

    # Test 2: LeetCode example 2 — k=3 ternary merges
    assert sol.mergeStones([3, 5, 1, 2, 6], 3) == 25

    # Test 3: Single merge possible in one step
    assert sol.mergeStones([1, 2, 3], 3) == 6

    # Test 4: Impossible — (4-1) % (3-1) = 1 ≠ 0
    assert sol.mergeStones([1, 2, 3, 4], 3) == -1

    # Test 5: Already one pile — no merges needed, cost 0
    assert sol.mergeStones([5], 3) == 0

    # Test 6: Two piles, k=2 — one merge
    assert sol.mergeStones([4, 6], 2) == 10

    print("All test cases passed.")
