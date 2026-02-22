from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        LeetCode #98 - Validate Binary Search Tree (Medium)

        Approach:
            DFS with tightening (low, high) bounds passed down the tree.
            Every node must satisfy low < node.val < high (strict inequalities
            since BST does not allow duplicates). The root starts with
            (-∞, +∞). Going left tightens the upper bound to the parent's
            value; going right tightens the lower bound. An iterative stack
            avoids Python's recursion limit on deep trees.

        Time Complexity:  O(n) — each node is visited at most once.
        Space Complexity: O(h) — stack depth bounded by the tree height.
        """
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, lo, hi = stack.pop()
            if not node:
                continue
            if not (lo < node.val < hi):
                return False
            stack.append((node.left,  lo,       node.val))
            stack.append((node.right, node.val, hi))
        return True


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


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid BST
    assert sol.isValidBST(build_tree([2, 1, 3])) is True

    # Test 2: Invalid — right child of 5 violates ancestor constraint
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    # 3 is in the right subtree of 5 but 3 < 5 → invalid
    assert sol.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False

    # Test 3: Single node
    assert sol.isValidBST(build_tree([1])) is True

    # Test 4: Duplicate values — not a valid BST
    assert sol.isValidBST(build_tree([2, 2, 2])) is False

    # Test 5: Classic pitfall — left ancestor bound must propagate right
    #   3
    #    \
    #     5
    #    /
    #   2       ← 2 < 3 violates the lower bound from ancestor 3
    root = build_tree([3, None, 5])
    root.right.left = TreeNode(2)
    assert sol.isValidBST(root) is False

    print("All test cases passed.")
