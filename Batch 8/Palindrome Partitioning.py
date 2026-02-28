from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        LeetCode #131 - Palindrome Partitioning (Medium)

        Approach — backtracking with DP palindrome precomputation:
            Precompute an n×n boolean table dp[i][j] = True if s[i..j] is a
            palindrome. This lets each palindrome check during backtracking
            cost O(1) instead of O(n).

            Backtrack from position `start`: for each end index j ≥ start,
            if dp[start][j] is True, append s[start..j] to the path and
            recurse from j+1. When start reaches n, the path is a complete
            valid partitioning — record a copy.

        Time Complexity:  O(n · 2^n) — up to 2^(n−1) partitions; each costs
                          O(n) to copy. DP precomputation is O(n²).
        Space Complexity: O(n²) for the DP table; O(n) recursion depth.
        """
        n = len(s)

        # Build palindrome DP table bottom-up
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        result: List[List[str]] = []
        path: List[str] = []

        def backtrack(start: int) -> None:
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1
    result = sol.partition("aab")
    assert sorted(result) == sorted([["a", "a", "b"], ["aa", "b"]])

    # Test 2: LeetCode example 2 — single character
    assert sol.partition("a") == [["a"]]

    # Test 3: Two identical characters
    assert sorted(sol.partition("aa")) == sorted([["a", "a"], ["aa"]])

    # Test 4: All distinct characters — only one partition (all singles)
    result = sol.partition("abc")
    assert sorted(result) == sorted([["a", "b", "c"]])

    # Test 5: Full palindrome — both all-singles and the whole string are valid
    result = sol.partition("aaa")
    assert sorted(result) == sorted([["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]])

    print("All test cases passed.")
