class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        LeetCode #76 - Minimum Window Substring (Hard)

        Approach:
            Variable-size sliding window with two frequency maps. The `need`
            map holds required counts from t; the `have` map tracks counts in
            the current window. A `formed` counter tracks how many distinct
            characters in t currently meet their required frequency. When
            `formed == required` the window is valid: record it, then advance
            the left pointer to try shrinking it. Expand right when invalid,
            contract left when valid.

        Time Complexity:  O(n + m) — n = len(s), m = len(t); each character
                          is added and removed from the window at most once.
        Space Complexity: O(m) — the frequency maps hold at most m distinct
                          characters from t.
        """
        if not t or not s:
            return ""

        need: dict[str, int] = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        have: dict[str, int] = {}
        formed = 0
        left = 0
        best_len = float("inf")
        best_left = 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_left = left

                out = s[left]
                have[out] -= 1
                if out in need and have[out] < need[out]:
                    formed -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_left: best_left + best_len]


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Classic LeetCode example
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    # Test 2: s == t
    assert sol.minWindow("a", "a") == "a"

    # Test 3: No valid window
    assert sol.minWindow("a", "b") == ""

    # Test 4: t has duplicate characters
    assert sol.minWindow("aa", "aa") == "aa"

    # Test 5: Minimum window is not at the start
    assert sol.minWindow("cabwefgewcwaefgcf", "cae") == "cwae"

    print("All test cases passed.")
