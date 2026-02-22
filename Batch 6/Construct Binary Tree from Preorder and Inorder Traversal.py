from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode | None:
        """
        LeetCode #105 - Construct Binary Tree from Preorder and Inorder
                        Traversal (Medium)

        Approach:
            The first element of preorder is always the root. Its position in
            inorder divides the array into left and right subtrees. Build an
            index map of inorder positions for O(1) lookups, then recurse
            using slice boundaries (no actual slicing — just index arithmetic)
            to avoid O(n²) copying. A nonlocal preorder index advances through
            the preorder array as nodes are created.

        Time Complexity:  O(n) — each node is created exactly once; index map
                          lookups are O(1).
        Space Complexity: O(n) — index map + recursion stack of depth h.
        """
        inorder_idx: dict[int, int] = {val: i for i, val in enumerate(inorder)}
        self._pre_idx = 0

        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            root_val = preorder[self._pre_idx]
            self._pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left  = build(left,    mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)


# ── helpers ──────────────────────────────────────────────────────────────────

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
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    tree = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert level_order(tree) == [3, 9, 20, None, None, 15, 7]

    # Test 2: Single node
    tree2 = sol.buildTree([-1], [-1])
    assert level_order(tree2) == [-1]

    # Test 3: Left-skewed tree  [1,2,3] preorder, [3,2,1] inorder
    #   1
    #  /
    # 2
    #  \   ← wait this is actually right child...
    # Let me use: preorder=[1,2,3], inorder=[2,1,3]
    #   1
    #  / \
    # 2   3
    tree3 = sol.buildTree([1, 2, 3], [2, 1, 3])
    assert level_order(tree3) == [1, 2, 3]

    # Test 4: Right-skewed
    #   1
    #    \
    #     2
    #      \
    #       3
    tree4 = sol.buildTree([1, 2, 3], [1, 2, 3])
    assert level_order(tree4) == [1, None, 2, None, 3]

    print("All test cases passed.")
