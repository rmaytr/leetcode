from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    LeetCode #297 - Serialize and Deserialize Binary Tree (Hard)

    Approach — preorder DFS with sentinel:
        Serialize: traverse in preorder (root → left → right). Represent each
        node as its integer value; represent absent children as the sentinel
        "N". Join tokens with commas into a single string.

        Deserialize: split the string on commas to recover the token list,
        wrap it in an iterator so each call to next() advances exactly one
        position, then recursively reconstruct the tree in the same preorder
        sequence. When the token is "N" the subtree is absent → return None.

    Why preorder? The root always comes first, so we can reconstruct the
    tree in one DFS pass without needing an inorder array for disambiguation.

    Time Complexity:  O(n) for both serialize and deserialize — each node
                      is processed exactly once.
    Space Complexity: O(n) for both — the string/token list and recursion
                      stack each scale with the number of nodes.
    """

    def serialize(self, root: TreeNode | None) -> str:
        tokens: list[str] = []

        def dfs(node: TreeNode | None) -> None:
            if not node:
                tokens.append("N")
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        it = iter(data.split(","))

        def dfs() -> TreeNode | None:
            token = next(it)
            if token == "N":
                return None
            node = TreeNode(int(token))
            node.left  = dfs()
            node.right = dfs()
            return node

        return dfs()


# ── helpers ──────────────────────────────────────────────────────────────────

def build_tree(values: list) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def trees_equal(a: TreeNode | None, b: TreeNode | None) -> bool:
    if not a and not b:
        return True
    if not a or not b or a.val != b.val:
        return False
    return trees_equal(a.left, b.left) and trees_equal(a.right, b.right)


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    codec = Codec()

    # Test 1: LeetCode example — serialize then deserialize recovers the tree
    original = build_tree([1, 2, 3, None, None, 4, 5])
    assert trees_equal(codec.deserialize(codec.serialize(original)), original)

    # Test 2: Empty tree
    assert codec.deserialize(codec.serialize(None)) is None

    # Test 3: Single node
    single = build_tree([42])
    assert trees_equal(codec.deserialize(codec.serialize(single)), single)

    # Test 4: Left-skewed tree
    skewed = build_tree([1, 2, None, 3, None, 4])
    assert trees_equal(codec.deserialize(codec.serialize(skewed)), skewed)

    # Test 5: Negative and zero values
    mixed = build_tree([-1, 0, -2])
    assert trees_equal(codec.deserialize(codec.serialize(mixed)), mixed)

    print("All test cases passed.")
