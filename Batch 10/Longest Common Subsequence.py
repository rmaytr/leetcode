class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        LeetCode #1143 - Longest Common Subsequence (Medium)

        Approach — 2D DP with space-optimised rolling rows:
            dp[i][j] = length of LCS of text1[:i] and text2[:j].
            Recurrence:
              • text1[i-1] == text2[j-1] → dp[i][j] = dp[i-1][j-1] + 1
              • otherwise             → dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            Keep only the previous row (`prev`) and current row (`curr`),
            reducing space from O(m × n) to O(min(m, n)) by always iterating
            over the shorter string.

        Time Complexity:  O(m × n).
        Space Complexity: O(min(m, n)) — single-row rolling array.
        """
        m, n = len(text1), len(text2)
        # Ensure text2 is the shorter string for minimal space
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m

        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return prev[n]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — LCS is "ace", length 3
    assert sol.longestCommonSubsequence("abcde", "ace") == 3

    # Test 2: LeetCode example 2 — identical strings, LCS is full string
    assert sol.longestCommonSubsequence("abc", "abc") == 3

    # Test 3: LeetCode example 3 — no common characters
    assert sol.longestCommonSubsequence("abc", "def") == 0

    # Test 4: One empty string
    assert sol.longestCommonSubsequence("", "abc") == 0
    assert sol.longestCommonSubsequence("abc", "") == 0

    # Test 5: s1 is a subsequence of s2 — full s1 is the LCS
    assert sol.longestCommonSubsequence("abcba", "abcbcba") == 5

    print("All test cases passed.")
