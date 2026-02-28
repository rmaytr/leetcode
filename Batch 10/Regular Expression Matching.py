class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        LeetCode #10 - Regular Expression Matching (Hard)

        Approach — bottom-up 2D DP:
            dp[i][j] = True iff s[:i] matches p[:j].
            Base cases:
              • dp[0][0] = True (empty matches empty).
              • dp[0][j] = dp[0][j-2] when p[j-1]=='*' (pattern "x*" can
                match zero of x, collapsing the last two pattern chars).
            Recurrence:
              • p[j-1] == '*':
                  zero occurrences → dp[i][j-2]
                  one+ occurrences → dp[i-1][j]  (if p[j-2] matches s[i-1])
              • p[j-1] == '.' or p[j-1] == s[i-1]:
                  dp[i][j] = dp[i-1][j-1]

        Time Complexity:  O(m × n) where m = len(s), n = len(p).
        Space Complexity: O(m × n).
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Empty string can match patterns like "a*", "a*b*", ".*" etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Zero occurrences of p[j-2]
                    dp[i][j] = dp[i][j - 2]
                    # One or more occurrences — p[j-2] must match s[i-1]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: 'a' does not match "aa"
    assert sol.isMatch("aa", "a") is False

    # Test 2: "a*" matches any run of a's, including "aa"
    assert sol.isMatch("aa", "a*") is True

    # Test 3: ".*" matches any string
    assert sol.isMatch("ab", ".*") is True

    # Test 4: LeetCode example — "c*" contributes zero c's, "a*" matches "aa"
    assert sol.isMatch("aab", "c*a*b") is True

    # Test 5: Empty string and pattern
    assert sol.isMatch("", "") is True
    assert sol.isMatch("", "a*") is True
    assert sol.isMatch("", "a") is False

    # Test 6: Dot wildcard
    assert sol.isMatch("abc", "a.c") is True
    assert sol.isMatch("abc", "a..") is True
    assert sol.isMatch("abc", "a.") is False

    print("All test cases passed.")
