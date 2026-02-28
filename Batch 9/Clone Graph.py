from __future__ import annotations
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None) -> None:
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        LeetCode #133 - Clone Graph (Medium)

        Approach — BFS with old→clone dictionary:
            Maintain a mapping from each original node to its deep clone. Seed
            the BFS queue with the start node and create its clone immediately.
            For every dequeued node, iterate its neighbors: create a clone if
            unseen (and enqueue the original), then append the neighbor's clone
            to the current clone's neighbor list.

        Time Complexity:  O(V + E) — each node and edge visited exactly once.
        Space Complexity: O(V) — clone map and BFS queue store at most V entries.
        """
        if not node:
            return None

        cloned: dict[Node, Node] = {node: Node(node.val)}
        queue: deque[Node] = deque([node])

        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in cloned:
                    cloned[nb] = Node(nb.val)
                    queue.append(nb)
                cloned[cur].neighbors.append(cloned[nb])

        return cloned[node]


# ── helpers ────────────────────────────────────────────────────────────────────

def build_graph(adj: list[list[int]]) -> Node | None:
    """Build a graph from a 1-indexed adjacency list; return node with val=1."""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def graph_to_adj(node: Node | None) -> list[list[int]]:
    """Convert a graph back to a sorted adjacency list for comparison."""
    if not node:
        return []
    visited: dict[int, Node] = {}
    queue: deque[Node] = deque([node])
    while queue:
        cur = queue.popleft()
        if cur.val in visited:
            continue
        visited[cur.val] = cur
        for nb in cur.neighbors:
            queue.append(nb)
    return [sorted(nb.val for nb in visited[v].neighbors) for v in sorted(visited)]


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example — 4-node cycle  1-2-3-4-1
    g = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    clone = sol.cloneGraph(g)
    assert graph_to_adj(clone) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert clone is not g  # deep copy — different objects

    # Test 2: Single node, no edges
    single = Node(1)
    clone2 = sol.cloneGraph(single)
    assert clone2.val == 1
    assert clone2.neighbors == []
    assert clone2 is not single

    # Test 3: Empty input
    assert sol.cloneGraph(None) is None

    # Test 4: Two nodes connected
    g4 = build_graph([[2], [1]])
    c4 = sol.cloneGraph(g4)
    assert graph_to_adj(c4) == [[2], [1]]

    print("All test cases passed.")
