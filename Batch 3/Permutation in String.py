class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        LeetCode #567 - Permutation in String (Medium)

        Approach:
            Fixed-size sliding window of length len(s1) over s2. Maintain two
            frequency arrays of size 26. Track how many of the 26 character
            counts currently match between the window and s1 (the `matches`
            counter). Slide the window one character at a time, updating only
            the two affected character slots and adjusting `matches` accordingly.
            When matches == 26, the window is an anagram of s1.

        Time Complexity:  O(n) — n = len(s2); each character processed once.
        Space Complexity: O(1) — two fixed arrays of 26 integers.
        """
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        have = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        k = len(s1)
        matches = 0

        # Build initial window
        for i in range(k):
            idx = ord(s2[i]) - ord('a')
            have[idx] += 1

        for i in range(26):
            if have[i] == need[i]:
                matches += 1

        if matches == 26:
            return True

        for right in range(k, len(s2)):
            # Add incoming character
            in_idx = ord(s2[right]) - ord('a')
            have[in_idx] += 1
            if have[in_idx] == need[in_idx]:
                matches += 1
            elif have[in_idx] == need[in_idx] + 1:
                matches -= 1

            # Remove outgoing character
            out_idx = ord(s2[right - k]) - ord('a')
            have[out_idx] -= 1
            if have[out_idx] == need[out_idx]:
                matches += 1
            elif have[out_idx] == need[out_idx] - 1:
                matches -= 1

            if matches == 26:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Permutation exists
    assert sol.checkInclusion("ab", "eidbaooo") is True

    # Test 2: No permutation
    assert sol.checkInclusion("ab", "eidboaoo") is False

    # Test 3: s1 longer than s2
    assert sol.checkInclusion("abc", "ab") is False

    # Test 4: Exact match
    assert sol.checkInclusion("abc", "cba") is True

    # Test 5: Single character
    assert sol.checkInclusion("a", "a") is True

    print("All test cases passed.")
