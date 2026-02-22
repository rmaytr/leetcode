import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        LeetCode #23 - Merge k Sorted Lists (Hard)

        Approach — min-heap over list heads:
            Push the head of each non-empty list onto a min-heap keyed by node
            value. Repeatedly pop the smallest node, append it to the result
            chain, and push its successor (if any). A monotonically increasing
            counter breaks value ties to avoid direct ListNode comparison.

        Time Complexity:  O(N log k) — N total nodes, each heap op is O(log k).
        Space Complexity: O(k) — heap holds at most one node per input list.
        """
        dummy = ListNode()
        tail = dummy
        heap: list = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        return dummy.next


# ── helpers ──────────────────────────────────────────────────────────────────

def build_list(values: list) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: ListNode | None) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(sol.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test 2: Empty input
    assert sol.mergeKLists([]) is None

    # Test 3: All empty lists
    assert sol.mergeKLists([None, None]) is None

    # Test 4: Single list passes through unchanged
    assert to_list(sol.mergeKLists([build_list([1, 2, 3])])) == [1, 2, 3]

    # Test 5: Lists with equal values — stable relative order preserved
    lists2 = [build_list([1, 1]), build_list([1, 1])]
    assert to_list(sol.mergeKLists(lists2)) == [1, 1, 1, 1]

    print("All test cases passed.")
