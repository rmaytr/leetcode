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

        Approach — Trie + DFS backtracking with pruning:
            Build a Trie from all target words so that shared prefixes are
            traversed only once. DFS from every board cell; at each step,
            follow the Trie branch for the current character. When we reach a
            terminal node (node.word is set), record the word and clear
            node.word to prevent duplicate reporting.

            Pruning: after exhausting a branch (no children remain), delete
            the leaf node from its parent's children dict. This prevents the
            DFS from revisiting dead Trie paths and dramatically reduces
            redundant work on large boards.

        Time Complexity:  O(M · 4 · 3^(L−1)) where M = number of board cells
                          and L = maximum word length — each DFS cell fans out
                          to at most 3 unvisited neighbours after the first step.
        Space Complexity: O(W · L) for the Trie (W words, average length L).
        """
        # Build trie from word list
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
            next_node = node.children[ch]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # dedup: each word reported once
            board[r][c] = "#"  # mark visited
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = ch  # restore
            # Prune exhausted trie branches to skip dead paths in future DFS
            if not next_node.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert sorted(sol.findWords(board1, ["oath", "pea", "eat", "rain"])) == sorted(["eat", "oath"])

    # Test 2: No words found
    board2 = [["a", "b"], ["c", "d"]]
    assert sol.findWords(board2, ["abcb"]) == []  # 'b' cannot be reused

    # Test 3: Single-cell board
    assert sol.findWords([["a"]], ["a"]) == ["a"]
    assert sol.findWords([["a"]], ["b"]) == []

    # Test 4: Word traces the entire board
    #   a b
    #   d c     path: a→b→c→d = "abcd"
    board3 = [["a", "b"], ["d", "c"]]
    assert sol.findWords(board3, ["abcd"]) == ["abcd"]

    # Test 5: Duplicate words in input — each reported only once
    board4 = [["a", "b"], ["c", "d"]]
    result = sol.findWords(board4, ["ab", "ab"])
    assert result.count("ab") == 1

    print("All test cases passed.")
