class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class WordDictionary:
    """
    LeetCode #211 - Design Add and Search Words Data Structure (Medium)

    Approach — Trie with DFS wildcard matching:
        Words are stored in a standard Trie (one node per character). The
        difference from a plain Trie is search: a '.' must match any single
        character, so when we encounter '.' we recursively try every child
        of the current node. Regular characters advance the trie normally;
        return False immediately if the character is absent.

    Time Complexity:  O(m) for addWord.
                      O(26^m) worst case for search when the pattern is all
                      dots — each position fans out to at most 26 children.
                      In practice patterns are sparse, so branching is limited.
    Space Complexity: O(Σ m_i) — one node per unique character prefix stored.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1: LeetCode example
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True

    # Test 2: All-wildcard pattern
    wd2 = WordDictionary()
    wd2.addWord("abc")
    assert wd2.search("...") is True
    assert wd2.search("....") is False  # length mismatch

    # Test 3: Empty word
    wd3 = WordDictionary()
    wd3.addWord("")
    assert wd3.search("") is True

    # Test 4: Wildcard must not match across word boundaries
    wd4 = WordDictionary()
    wd4.addWord("at")
    wd4.addWord("and")
    assert wd4.search("a.") is True    # matches "at"
    assert wd4.search("a..") is True   # matches "and"
    assert wd4.search("a...") is False

    print("All test cases passed.")
