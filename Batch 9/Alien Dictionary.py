from typing import List
from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        LeetCode #269 - Alien Dictionary (Hard)

        Approach — topological sort on character ordering constraints:
            Compare each consecutive word pair to extract ordering: the first
            differing character gives a directed edge u → v (u precedes v in
            the alien alphabet). Edge cases:
              • If word[i] is longer than word[i+1] but word[i+1] is a prefix
                of word[i], the ordering is impossible → return "".
              • Only the first differing character per pair matters.

            Build a directed graph (≤ 26 nodes) and run Kahn's BFS topological
            sort. If all characters are processed, return the order; if a cycle
            is detected (unprocessed characters remain), return "".

        Time Complexity:  O(C) where C = total characters across all words.
        Space Complexity: O(1) — graph bounded by 26 unique characters.
        """
        adj: dict[str, list[str]] = {ch: [] for word in words for ch in word}
        in_degree: dict[str, int] = {ch: 0 for ch in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # Longer word before its own prefix — impossible ordering
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    in_degree[w2[j]] += 1
                    break  # only first differing character matters

        queue: deque[str] = deque(
            ch for ch, deg in in_degree.items() if deg == 0
        )
        result: list[str] = []

        while queue:
            ch = queue.popleft()
            result.append(ch)
            for nb in adj[ch]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    queue.append(nb)

        return "".join(result) if len(result) == len(in_degree) else ""


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — derives w→e, e→r, r→t, t→f
    result1 = sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    assert result1 == "wertf"

    # Test 2: LeetCode example 2 — z before x
    result2 = sol.alienOrder(["z", "x"])
    assert result2 == "zx"

    # Test 3: Cycle detected → empty string
    result3 = sol.alienOrder(["z", "x", "z"])
    assert result3 == ""

    # Test 4: Longer word precedes its prefix → impossible
    result4 = sol.alienOrder(["abc", "ab"])
    assert result4 == ""

    # Test 5: Single word — no ordering constraints; all chars are valid
    result5 = sol.alienOrder(["abc"])
    assert set(result5) == {"a", "b", "c"}

    print("All test cases passed.")
