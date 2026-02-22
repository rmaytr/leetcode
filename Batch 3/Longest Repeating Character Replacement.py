class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        LeetCode #424 - Longest Repeating Character Replacement (Medium)

        Approach:
            Sliding window. A window is valid when:
                (window length) - (count of most frequent char) <= k
            because we can replace the minority characters using at most k
            operations. We track the running maximum frequency seen so far
            (max_freq). Note: max_freq may be slightly optimistic after the
            left pointer advances, but this only means the window never
            shrinks — it stays the same size or grows. This is safe because
            we only care about the maximum valid window ever reached.

        Time Complexity:  O(n) — each character is processed once; the
                          frequency array has constant size (26 letters).
        Space Complexity: O(1) — fixed-size frequency array of 26 entries.
        """
        count = [0] * 26
        left = 0
        max_freq = 0
        best = 0
        for right, ch in enumerate(s):
            count[ord(ch) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(ch) - ord('A')])
            window_len = right - left + 1
            if window_len - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example — replace 1 char in "AABA"
    assert sol.characterReplacement("AABABBA", 1) == 4

    # Test 2: Replace up to 2 in all-same string
    assert sol.characterReplacement("AAAA", 2) == 4

    # Test 3: Two character types, large k
    assert sol.characterReplacement("ABAB", 2) == 4

    # Test 4: k = 0 — no replacements allowed
    assert sol.characterReplacement("AABBA", 0) == 2

    # Test 5: Single character
    assert sol.characterReplacement("A", 1) == 1

    print("All test cases passed.")
