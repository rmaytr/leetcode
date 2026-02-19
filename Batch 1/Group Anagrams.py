from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        LeetCode #49 - Group Anagrams (Medium)

        Approach:
            Use a fixed-length tuple of 26 character counts as the hash key.
            This avoids sorting (O(k log k) per word) and works in O(k) per
            word. All words that are anagrams of each other will produce an
            identical count tuple and therefore map to the same bucket.

        Time Complexity:  O(n * k) — n words each of max length k.
        Space Complexity: O(n * k) — storing all words in the hash map.
        """
        groups: dict[tuple, List[str]] = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case — order of groups doesn't matter
    result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result_sorted = sorted(sorted(g) for g in result)
    assert result_sorted == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    # Test 2: Single empty string
    assert sol.groupAnagrams([""]) == [[""]]

    # Test 3: Single character
    assert sol.groupAnagrams(["a"]) == [["a"]]

    print("All test cases passed.")
