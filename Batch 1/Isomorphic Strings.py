class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        LeetCode #205 - Isomorphic Strings (Easy)

        Approach:
            Maintain two dictionaries: one mapping characters of s → t, and
            one mapping t → s. For each pair of characters at the same index,
            verify that any existing mapping is consistent in both directions.
            A bidirectional check prevents cases like s="badc", t="baba"
            where a one-way map would incorrectly pass.

        Time Complexity:  O(n) — single pass over both strings.
        Space Complexity: O(1) — maps are bounded by the alphabet size (≤256).
        """
        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}

        for cs, ct in zip(s, t):
            if s_to_t.get(cs, ct) != ct or t_to_s.get(ct, cs) != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs

        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid isomorphism
    assert sol.isIsomorphic("egg", "add") is True

    # Test 2: Not isomorphic
    assert sol.isIsomorphic("foo", "bar") is False

    # Test 3: Valid (every char maps to itself)
    assert sol.isIsomorphic("paper", "title") is True

    # Test 4: Two chars mapping to same char
    assert sol.isIsomorphic("badc", "baba") is False

    print("All test cases passed.")
