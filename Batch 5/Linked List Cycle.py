class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """
        LeetCode #141 - Linked List Cycle (Easy)

        Approach:
            Floyd's tortoise-and-hare algorithm. The slow pointer advances one
            node per step; the fast pointer advances two. If a cycle exists,
            fast will lap slow and they will meet inside the cycle. If no cycle
            exists, fast (or fast.next) will reach None and we return False.

        Time Complexity:  O(n) — fast pointer reaches the cycle entry or tail
                          within n steps; once inside the cycle it laps slow
                          within at most the cycle length steps.
        Space Complexity: O(1) — only two pointer variables.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# ── helpers ──────────────────────────────────────────────────────────────────

def build_cycle_list(values: list[int], pos: int) -> ListNode | None:
    """Build a linked list; if pos >= 0 the tail connects back to node at pos."""
    if not values:
        return None
    dummy = ListNode()
    cur = dummy
    nodes = []
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
        nodes.append(cur)
    if pos >= 0:
        nodes[-1].next = nodes[pos]  # create cycle
    return dummy.next


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Cycle at position 1
    assert sol.hasCycle(build_cycle_list([3, 2, 0, -4], 1)) is True

    # Test 2: Cycle at position 0 (head)
    assert sol.hasCycle(build_cycle_list([1, 2], 0)) is True

    # Test 3: No cycle — single node
    assert sol.hasCycle(build_cycle_list([1], -1)) is False

    # Test 4: No cycle — multiple nodes
    assert sol.hasCycle(build_cycle_list([1, 2, 3, 4], -1)) is False

    # Test 5: Empty list
    assert sol.hasCycle(None) is False

    print("All test cases passed.")
