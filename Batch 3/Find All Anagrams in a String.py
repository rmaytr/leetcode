from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        LeetCode #438 - Find All Anagrams in a String (Medium)

        Approach:
            Fixed-size sliding window identical to Permutation in String, but
            we collect every starting index where the window is a valid anagram
            instead of returning early. Use a `matches` counter over 26
            character slots so each slide only touches two slots in O(1),
            giving a clean linear scan with no repeated comparisons.

        Time Complexity:  O(n) — n = len(s); each character processed once.
        Space Complexity: O(1) — two fixed-size arrays of 26 integers plus the
                          output list (not counted against auxiliary space).
        """
        result = []
        if len(p) > len(s):
            return result

        need = [0] * 26
        have = [0] * 26
        for ch in p:
            need[ord(ch) - ord('a')] += 1

        k = len(p)

        # Build initial window
        for i in range(k):
            have[ord(s[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if have[i] == need[i])
        if matches == 26:
            result.append(0)

        for right in range(k, len(s)):
            # Add incoming character
            in_idx = ord(s[right]) - ord('a')
            have[in_idx] += 1
            if have[in_idx] == need[in_idx]:
                matches += 1
            elif have[in_idx] == need[in_idx] + 1:
                matches -= 1

            # Remove outgoing character
            out_idx = ord(s[right - k]) - ord('a')
            have[out_idx] -= 1
            if have[out_idx] == need[out_idx]:
                matches += 1
            elif have[out_idx] == need[out_idx] - 1:
                matches -= 1

            if matches == 26:
                result.append(right - k + 1)

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Multiple anagrams
    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]

    # Test 2: Consecutive anagrams
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]

    # Test 3: No anagram
    assert sol.findAnagrams("af", "be") == []

    # Test 4: Entire string is the anagram
    assert sol.findAnagrams("cba", "abc") == [0]

    # Test 5: p longer than s
    assert sol.findAnagrams("ab", "abc") == []

    print("All test cases passed.")
