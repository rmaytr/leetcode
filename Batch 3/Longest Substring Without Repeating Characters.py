class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LeetCode #3 - Longest Substring Without Repeating Characters (Medium)

        Approach:
            Variable-size sliding window with a hash map that stores each
            character's most recent index. The left pointer jumps directly to
            one position past the previous occurrence of a repeated character,
            skipping over the duplicate in O(1) rather than shrinking the
            window one step at a time. The window [left, right] is always
            duplicate-free.

        Time Complexity:  O(n) — right pointer visits each character once;
                          left pointer only moves forward.
        Space Complexity: O(min(n, m)) — map holds at most m distinct
                          characters (m = alphabet size, 128 for ASCII).
        """
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            length = right - left + 1
            if length > best:
                best = length
        return best


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Classic LeetCode example
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3

    # Test 2: All same characters
    assert sol.lengthOfLongestSubstring("bbbbb") == 1

    # Test 3: Mixed repeats
    assert sol.lengthOfLongestSubstring("pwwkew") == 3

    # Test 4: Empty string
    assert sol.lengthOfLongestSubstring("") == 0

    # Test 5: All unique characters
    assert sol.lengthOfLongestSubstring("abcdef") == 6

    # Test 6: Repeat not adjacent — window must not shrink too far
    assert sol.lengthOfLongestSubstring("abba") == 2

    print("All test cases passed.")
