from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        LeetCode #100 - Same Tree (Easy)

        Approach:
            Iterative BFS using a deque of node pairs. For each pair dequeued,
            check the four base cases: both None (matching absence → continue),
            one None (structural mismatch → False), or unequal values → False.
            If all pairs match, return True. Iterative BFS avoids recursion-
            depth issues on very deep trees.

        Time Complexity:  O(n) — every node pair is visited at most once;
                          n = min(|p|, |q|) in the mismatch case, |p| = |q|
                          when trees are identical.
        Space Complexity: O(w) — deque width bounded by the widest level.
        """
        queue = deque([(p, q)])
        while queue:
            a, b = queue.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            queue.append((a.left, b.left))
            queue.append((a.right, b.right))
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

    # Test 1: Identical trees
    assert sol.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True

    # Test 2: Different structure
    assert sol.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False

    # Test 3: Different values
    assert sol.isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False

    # Test 4: Both empty
    assert sol.isSameTree(None, None) is True

    # Test 5: One empty, one not
    assert sol.isSameTree(build_tree([1]), None) is False

    # Test 6: Deeper identical trees
    assert sol.isSameTree(
        build_tree([1, 2, 3, 4, 5]),
        build_tree([1, 2, 3, 4, 5])
    ) is True

    print("All test cases passed.")
