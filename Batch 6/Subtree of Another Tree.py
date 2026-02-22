from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        LeetCode #572 - Subtree of Another Tree (Easy)

        Approach:
            For every node in `root`, call isSameTree with that node and
            `subRoot`. If any call returns True, subRoot is a subtree. The
            recursion naturally handles the None base case: a None root cannot
            contain any non-None subRoot, while a None subRoot is a subtree of
            everything.

            isSameTree itself is a simple recursive structural comparison
            factored out as a private helper for clarity.

        Time Complexity:  O(m * n) — for each of the m nodes in root we may
                          run a full O(n) same-tree check (n = nodes in subRoot).
        Space Complexity: O(h_root) — recursion stack depth bounded by the
                          height of the main tree.
        """
        if not root:
            return False
        if self._same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self._same(p.left, q.left) and self._same(p.right, q.right)


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

    # Test 1: subRoot is the left subtree of root
    assert sol.isSubtree(
        build_tree([3, 4, 5, 1, 2]),
        build_tree([4, 1, 2])
    ) is True

    # Test 2: subRoot has an extra child — not a subtree
    assert sol.isSubtree(
        build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
        build_tree([4, 1, 2])
    ) is False

    # Test 3: subRoot equals root
    assert sol.isSubtree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True

    # Test 4: subRoot is a single leaf in root
    assert sol.isSubtree(build_tree([1, 2, 3]), build_tree([3])) is True

    # Test 5: subRoot not present anywhere
    assert sol.isSubtree(build_tree([1, 2, 3]), build_tree([4])) is False

    print("All test cases passed.")
