class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        LeetCode #115 - Distinct Subsequences (Hard)

        Approach — 1D DP (space-optimised 2D table):
            dp[j] = number of ways t[:j] appears as a subsequence of the
            portion of s processed so far.
            Base: dp[0] = 1 (empty t is always a subsequence).
            For each character s[i-1], iterate j from len(t) down to 1
            (right-to-left to avoid using updated values from the same row):
              • if s[i-1] == t[j-1]: dp[j] += dp[j-1]
                (we can either match this s character with t[j-1], using dp[j-1]
                 ways to match t[:j-1], or skip it, keeping the existing dp[j])

        Time Complexity:  O(m × n) where m = len(s), n = len(t).
        Space Complexity: O(n) — single DP array of length n+1.
        """
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t is a subsequence of any prefix of s

        for i in range(1, m + 1):
            for j in range(n, 0, -1):   # right-to-left avoids stale reads
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — 3 ways to form "rabbit" from "rabbbit"
    assert sol.numDistinct("rabbbit", "rabbit") == 3

    # Test 2: LeetCode example 2 — 5 ways to form "bag" from "babgbag"
    assert sol.numDistinct("babgbag", "bag") == 5

    # Test 3: t longer than s — impossible
    assert sol.numDistinct("a", "ab") == 0

    # Test 4: No matching characters
    assert sol.numDistinct("abc", "xyz") == 0

    # Test 5: t is empty — exactly 1 subsequence (the empty one)
    assert sol.numDistinct("abc", "") == 1

    # Test 6: Exact match
    assert sol.numDistinct("abc", "abc") == 1

    print("All test cases passed.")
