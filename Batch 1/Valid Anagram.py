class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        LeetCode #242 - Valid Anagram (Easy)

        Approach:
            Early-exit on length mismatch. Build a frequency counter for the
            characters in s, then decrement counts for characters in t.
            Any non-zero count at the end means the strings are not anagrams.
            Using a plain dict is faster than Counter for small alphabets.

        Time Complexity:  O(n) — two linear passes over strings of length n.
        Space Complexity: O(1) — at most 26 distinct lowercase letters stored.
        """
        if len(s) != len(t):
            return False

        count: dict[str, int] = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]

        return len(count) == 0


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid anagram
    assert sol.isAnagram("anagram", "nagaram") is True

    # Test 2: Not an anagram
    assert sol.isAnagram("rat", "car") is False

    # Test 3: Different lengths
    assert sol.isAnagram("ab", "a") is False

    # Test 4: Empty strings
    assert sol.isAnagram("", "") is True

    print("All test cases passed.")
