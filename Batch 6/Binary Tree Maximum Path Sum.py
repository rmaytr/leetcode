from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        """
        LeetCode #124 - Binary Tree Maximum Path Sum (Hard)

        Approach:
            Post-order DFS. For each node, compute the maximum "gain" each
            child subtree can contribute to a path passing through the current
            node — clamped to 0 so we never extend through a net-negative
            subtree. The candidate path sum through the current node is:
                node.val + left_gain + right_gain
            Update the global maximum with this candidate, then return only
            node.val + max(left_gain, right_gain) to the parent, because a
            path extending upward can fork in only one direction.

        Time Complexity:  O(n) — each node is visited exactly once.
        Space Complexity: O(h) — recursion stack; O(log n) balanced,
                          O(n) worst-case skewed tree.
        """
        self._max = float("-inf")

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            left_gain  = max(dfs(node.left),  0)
            right_gain = max(dfs(node.right), 0)
            self._max = max(self._max, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self._max


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

    # Test 1: LeetCode example 1 — path 1→2→3
    assert sol.maxPathSum(build_tree([1, 2, 3])) == 6

    # Test 2: LeetCode example 2 — path 15→20→7
    assert sol.maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42

    # Test 3: All negative — best single node
    assert sol.maxPathSum(build_tree([-3])) == -3

    # Test 4: All negative tree — must pick the least-negative node
    assert sol.maxPathSum(build_tree([-1, -2, -3])) == -1

    # Test 5: Path goes through the root connecting two long arms
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5    → best path: 4→2→1→3→5 = 15
    root = build_tree([1, 2, 3])
    root.left.left   = TreeNode(4)
    root.right.right = TreeNode(5)
    assert sol.maxPathSum(root) == 15

    print("All test cases passed.")
