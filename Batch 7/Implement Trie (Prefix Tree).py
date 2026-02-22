class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class Trie:
    """
    LeetCode #208 - Implement Trie (Prefix Tree) (Medium)

    Approach — linked TrieNode with children dict:
        Each node stores a dict mapping character → child TrieNode and a
        boolean flagging end-of-word. insert, search, and startsWith each
        walk the trie one character at a time and return early when a
        character is missing from the current node's children. A dict (vs a
        fixed 26-slot array) keeps memory proportional to characters actually
        stored.

    Time Complexity:  O(m) per operation, where m is the word/prefix length.
    Space Complexity: O(Σ m_i) — one node per unique character prefix across
                      all inserted words.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1: LeetCode example
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True

    # Test 2: Prefix exists but word was not inserted
    trie2 = Trie()
    trie2.insert("hello")
    assert trie2.search("hell") is False
    assert trie2.startsWith("hell") is True

    # Test 3: Empty prefix always matches any non-empty trie
    trie3 = Trie()
    trie3.insert("a")
    assert trie3.startsWith("") is True

    # Test 4: Word not in trie and no shared prefix
    trie4 = Trie()
    trie4.insert("cat")
    assert trie4.search("car") is False
    assert trie4.startsWith("dog") is False

    print("All test cases passed.")
