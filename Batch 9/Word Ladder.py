from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        LeetCode #127 - Word Ladder (Hard)

        Approach — bidirectional BFS:
            Standard BFS explores O(b^d) nodes (b = branching factor, d = depth).
            Bidirectional BFS maintains two frontiers (one from beginWord, one
            from endWord) and always expands the smaller one, reducing the search
            space to roughly O(b^(d/2)) per side.

            At each step, generate all single-character variants of each word in
            the current frontier. If a variant appears in the opposite frontier,
            the path is complete — return the current length. Otherwise, add
            valid variants (present in the word set) to the next frontier and
            remove them from the word set to prevent revisits.

        Time Complexity:  O(M² × N) where M = word length, N = |wordList|.
        Space Complexity: O(M × N) — frontiers and word set.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        front: set[str] = {beginWord}
        back: set[str] = {endWord}
        length = 1

        while front:
            length += 1
            if len(front) > len(back):
                front, back = back, front
            nxt: set[str] = set()
            for word in front:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + ch + word[i + 1:]
                        if candidate in back:
                            return length
                        if candidate in word_set:
                            nxt.add(candidate)
                            word_set.discard(candidate)
            front = nxt

        return 0


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — hit→hot→dot→dog→cog (5 steps)
    assert sol.ladderLength(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
    ) == 5

    # Test 2: LeetCode example 2 — endWord not reachable
    assert sol.ladderLength(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log"]
    ) == 0

    # Test 3: Direct one-step transformation
    assert sol.ladderLength("ab", "cb", ["cb"]) == 2

    # Test 4: endWord not in wordList at all
    assert sol.ladderLength("a", "c", ["a", "b"]) == 0

    # Test 5: Two-step path
    assert sol.ladderLength("hot", "dog", ["hot", "dot", "dog"]) == 3

    print("All test cases passed.")
