class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        LeetCode #72 - Edit Distance (Hard)

        Approach — 2D DP with space-optimised rolling rows:
            dp[i][j] = minimum edits (insert, delete, replace) to transform
            word1[:i] into word2[:j].
            Base cases: dp[0][j] = j (insert j chars), dp[i][0] = i (delete i chars).
            Recurrence:
              • word1[i-1] == word2[j-1] → dp[i][j] = dp[i-1][j-1]  (no op)
              • otherwise → dp[i][j] = 1 + min(
                    dp[i-1][j-1],   # replace
                    dp[i-1][j],     # delete from word1
                    dp[i][j-1]      # insert into word1
                )
            Keep only two rows to reduce space to O(n).

        Time Complexity:  O(m × n).
        Space Complexity: O(n) — rolling two-row DP.
        """
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))   # dp[0][0..n]

        for i in range(1, m + 1):
            curr = [i] + [0] * n    # dp[i][0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j - 1],   # replace
                        prev[j],       # delete
                        curr[j - 1],   # insert
                    )
            prev = curr

        return prev[n]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — horse→rorse→rose→ros, 3 edits
    assert sol.minDistance("horse", "ros") == 3

    # Test 2: LeetCode example 2
    assert sol.minDistance("intention", "execution") == 5

    # Test 3: Empty strings
    assert sol.minDistance("", "") == 0
    assert sol.minDistance("abc", "") == 3
    assert sol.minDistance("", "abc") == 3

    # Test 4: Identical strings — 0 edits
    assert sol.minDistance("kitten", "kitten") == 0

    # Test 5: Single character operations
    assert sol.minDistance("a", "b") == 1   # replace
    assert sol.minDistance("ab", "a") == 1  # delete

    print("All test cases passed.")
