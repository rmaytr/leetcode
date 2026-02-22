class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        """
        LeetCode #138 - Copy List with Random Pointer (Medium)

        Approach:
            Hash map from each original node to its deep-copy counterpart.
            First pass: create all copy nodes (values only, no links).
            Second pass: wire up next and random pointers using the map.
            Using a defaultdict that auto-creates a copy node on first access
            allows both passes to be collapsed into one elegant loop — but the
            explicit two-pass version is shown here for maximum clarity.

        Time Complexity:  O(n) — two linear passes.
        Space Complexity: O(n) — the hash map holds one entry per node.
        """
        if not head:
            return None

        old_to_new: dict[Node, Node] = {}

        # Pass 1: create all copy nodes
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # Pass 2: wire next and random
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next   = old_to_new.get(cur.next)
            copy.random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]


# ── helpers ──────────────────────────────────────────────────────────────────

def build_random_list(data: list[tuple[int, int | None]]) -> Node | None:
    """
    data is a list of (val, random_index) pairs; random_index is the 0-based
    index of the node the random pointer points to, or None.
    """
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (_, rand_idx) in enumerate(data):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]


def to_list_with_random(head: Node | None) -> list[tuple[int, int | None]]:
    """Return [(val, random_index_or_None), ...] for easy assertion."""
    nodes, result = [], []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    index = {node: i for i, node in enumerate(nodes)}
    for node in nodes:
        result.append((node.val, index.get(node.random)))
    return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    original = build_random_list([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
    copied = sol.copyRandomList(original)
    assert to_list_with_random(copied) == [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]

    # Test 2: Deep copy — nodes must be different objects
    assert copied is not original
    cur_o, cur_c = original, copied
    while cur_o:
        assert cur_o is not cur_c
        cur_o, cur_c = cur_o.next, cur_c.next

    # Test 3: Single node, random points to itself
    original2 = build_random_list([(1, 0)])
    copied2 = sol.copyRandomList(original2)
    assert to_list_with_random(copied2) == [(1, 0)]

    # Test 4: Empty list
    assert sol.copyRandomList(None) is None

    print("All test cases passed.")
