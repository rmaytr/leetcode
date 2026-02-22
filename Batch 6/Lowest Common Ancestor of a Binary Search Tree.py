from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        LeetCode #235 - Lowest Common Ancestor of a Binary Search Tree (Medium)

        Approach:
            Exploit the BST ordering property iteratively. At each node:
            - If both p and q are less than the current value, the LCA must
              lie in the left subtree → move left.
            - If both are greater, the LCA must lie in the right subtree
              → move right.
            - Otherwise the current node is the split point, meaning one target
              is in each subtree (or one target IS the current node), so the
              current node is the LCA.

        Time Complexity:  O(h) — at most one traversal down a root-to-leaf path;
                          h = O(log n) for a balanced BST, O(n) worst case.
        Space Complexity: O(1) — iterative; no recursion stack.
        """
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        return cur  # unreachable for valid inputs


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


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    """Return the node with the given value via BST search."""
    while root:
        if val == root.val:
            return root
        root = root.left if val < root.val else root.right
    return None


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    #       6
    #      / \
    #     2   8
    #    / \ / \
    #   0  4 7  9
    #     / \
    #    3   5
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

    # Test 1: LCA of 2 and 8 is 6 (root)
    assert sol.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 8)).val == 6

    # Test 2: LCA of 2 and 4 is 2 (p is ancestor of q)
    assert sol.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 4)).val == 2

    # Test 3: LCA of 3 and 5 is 4
    assert sol.lowestCommonAncestor(root, find_node(root, 3), find_node(root, 5)).val == 4

    # Test 4: LCA of 7 and 9 is 8
    assert sol.lowestCommonAncestor(root, find_node(root, 7), find_node(root, 9)).val == 8

    # Test 5: Same node (p == q)
    assert sol.lowestCommonAncestor(root, find_node(root, 4), find_node(root, 4)).val == 4

    print("All test cases passed.")
