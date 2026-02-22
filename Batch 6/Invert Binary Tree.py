from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        LeetCode #226 - Invert Binary Tree (Easy)

        Approach:
            Recursive post-order DFS. Recurse into both subtrees first, then
            swap the two children of the current node. Swapping after recursing
            is equivalent to swapping before — both produce the same mirrored
            tree — but post-order makes the intent clear: fix children, then
            fix parent.

        Time Complexity:  O(n) — every node is visited exactly once.
        Space Complexity: O(h) — implicit recursion stack; h = tree height.
                          O(log n) for a balanced tree, O(n) worst case (skewed).
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# ── helpers ──────────────────────────────────────────────────────────────────

def build_tree(values: list) -> TreeNode | None:
    """Construct a binary tree from a level-order list (None = absent node)."""
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


def level_order(root: TreeNode | None) -> list:
    """Return level-order values, trimming trailing Nones."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    #     4              4
    #    / \    →       / \
    #   2   7          7   2
    #  / \ / \        / \ / \
    # 1  3 6  9      9  6 3  1
    assert level_order(sol.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]

    # Test 2: Single node
    assert level_order(sol.invertTree(build_tree([1]))) == [1]

    # Test 3: Empty tree
    assert sol.invertTree(None) is None

    # Test 4: Two-level tree
    assert level_order(sol.invertTree(build_tree([1, 2, 3]))) == [1, 3, 2]

    print("All test cases passed.")
