import sys
from typing import List

sys.setrecursionlimit(200_000)


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        LeetCode #1192 - Critical Connections in a Network (Hard)

        Approach — Tarjan's bridge-finding algorithm:
            Perform a DFS and assign each node a discovery timestamp (disc[v]).
            Also track low[v] = the earliest timestamp reachable from v's
            subtree via back-edges (excluding the direct parent edge).
            An edge (u, v) is a bridge if low[v] > disc[u]: the subtree rooted
            at v has no back-edge reaching u or any ancestor of u, so removing
            (u, v) disconnects the graph.

        Time Complexity:  O(V + E) — single DFS traversal.
        Space Complexity: O(V + E) — adjacency list, disc/low arrays, call stack.
        """
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        disc: list[int] = [-1] * n
        low: list[int] = [0] * n
        timer = [0]
        bridges: list[list[int]] = []

        def dfs(u: int, parent: int) -> None:
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            for v in adj[u]:
                if disc[v] == -1:           # tree edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:    # bridge condition
                        bridges.append([u, v])
                elif v != parent:           # back edge (skip undirected parent)
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)
        return bridges


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example — triangle plus dangling node; [1,3] is the bridge
    result1 = sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
    assert result1 == [[1, 3]]

    # Test 2: Linear chain — every edge is a bridge
    result2 = sorted(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 3]]))
    assert result2 == sorted([[0, 1], [1, 2], [2, 3]])

    # Test 3: Triangle — every edge is in a cycle, no bridges
    result3 = sol.criticalConnections(3, [[0, 1], [1, 2], [0, 2]])
    assert result3 == []

    # Test 4: Two nodes, single edge — that edge is a bridge
    result4 = sol.criticalConnections(2, [[0, 1]])
    assert result4 == [[0, 1]]

    # Test 5: Two triangles sharing one bridge edge
    # 0-1-2-0  connected to  3-4-5-3  via bridge 2-3
    conns5 = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [5, 3]]
    result5 = sol.criticalConnections(6, conns5)
    assert result5 == [[2, 3]]

    print("All test cases passed.")
