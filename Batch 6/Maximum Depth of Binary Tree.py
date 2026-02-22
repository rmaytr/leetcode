from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        LeetCode #104 - Maximum Depth of Binary Tree (Easy)

        Approach:
            Iterative BFS level-by-level. Use a deque; each time we fully
            process one level we increment the depth counter. BFS is preferred
            over recursive DFS here because it avoids stack-overflow risk on
            very deep skewed trees and keeps the space bounded by the widest
            level rather than the height.

        Time Complexity:  O(n) — every node is dequeued exactly once.
        Space Complexity: O(w) — deque holds at most one full level at a time;
                          w = maximum tree width (up to n/2 for a complete tree).
        """
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


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

    # Test 1: LeetCode example — balanced tree of depth 3
    assert sol.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3

    # Test 2: Single node
    assert sol.maxDepth(build_tree([1])) == 1

    # Test 3: Empty tree
    assert sol.maxDepth(None) == 0

    # Test 4: Left-skewed tree (depth == node count)
    assert sol.maxDepth(build_tree([1, 2, None, 3, None, 4])) == 4

    # Test 5: Complete balanced tree of depth 4
    assert sol.maxDepth(build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 4

    print("All test cases passed.")
