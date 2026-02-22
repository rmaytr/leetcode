from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
        """
        LeetCode #102 - Binary Tree Level Order Traversal (Medium)

        Approach:
            BFS with a deque. Before processing each level, snapshot the
            current queue size — that tells us exactly how many nodes belong
            to the current level. Dequeue that many nodes, collect their
            values into a level list, and enqueue their non-None children.
            Repeat until the queue is empty.

        Time Complexity:  O(n) — each node is enqueued and dequeued once.
        Space Complexity: O(w) — deque holds at most one full level; the
                          widest level of a complete binary tree has n/2 nodes.
        """
        if not root:
            return []
        result: List[List[int]] = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level: List[int] = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


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

    # Test 1: LeetCode example
    assert sol.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]

    # Test 2: Single node
    assert sol.levelOrder(build_tree([1])) == [[1]]

    # Test 3: Empty tree
    assert sol.levelOrder(None) == []

    # Test 4: Perfect binary tree — 4 levels
    assert sol.levelOrder(build_tree([1, 2, 3, 4, 5, 6, 7])) == [[1], [2, 3], [4, 5, 6, 7]]

    # Test 5: Left-skewed tree
    assert sol.levelOrder(build_tree([1, 2, None, 3, None, 4])) == [[1], [2], [3], [4]]

    print("All test cases passed.")
