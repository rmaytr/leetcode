from typing import List


class TrieNode:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None  # non-None only at word-terminal nodes


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        LeetCode #212 - Word Search II (Hard)

        Approach — Trie construction + DFS backtracking with branch pruning:
            Build a Trie from all target words so that shared prefixes are
            explored only once. DFS from every board cell using the same
            in-place '#' marking as Word Search (#79). At each step, follow
            the Trie branch for the current character; if the branch doesn't
            exist, return early (prefix pruning). When a terminal node is
            reached, record the word and clear node.word to prevent duplicates.

            After exhausting a DFS subtree, delete leaf Trie nodes from their
            parent (structural pruning). This progressively shrinks the Trie,
            dramatically reducing redundant DFS calls on large boards.

        Time Complexity:  O(M · 4 · 3^(L−1)) where M = board cells and
                          L = maximum word length.
        Space Complexity: O(W · L) for the Trie (W words, average length L).
        """
        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result: List[str] = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # prevent duplicate reporting
            board[r][c] = "#"  # mark visited (backtracking)
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch  # restore (backtrack)
            # Structural pruning: remove exhausted leaf nodes
            if not nxt.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert sorted(sol.findWords(board1, ["oath", "pea", "eat", "rain"])) == sorted(["eat", "oath"])

    # Test 2: No words found — 'b' cannot be reused
    board2 = [["a", "b"], ["c", "d"]]
    assert sol.findWords(board2, ["abcb"]) == []

    # Test 3: Single-cell board
    assert sol.findWords([["a"]], ["a"]) == ["a"]
    assert sol.findWords([["a"]], ["b"]) == []

    # Test 4: Word traces the whole board — a→b→c→d
    board3 = [["a", "b"], ["d", "c"]]
    assert sol.findWords(board3, ["abcd"]) == ["abcd"]

    # Test 5: Duplicate words in input — each reported exactly once
    board4 = [["a", "b"], ["c", "d"]]
    assert sol.findWords(board4, ["ab", "ab"]).count("ab") == 1

    print("All test cases passed.")
