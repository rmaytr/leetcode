import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode | None]) -> ListNode | None:
        """
        LeetCode #23 - Merge k Sorted Lists (Hard)

        Approach:
            Min-heap over the current front nodes of all k lists. Each heap
            entry is a (value, tie_breaker, node) tuple; the integer
            tie_breaker prevents Python from comparing ListNode objects when
            values are equal. Pop the minimum, attach it to the result, and
            push its successor (if any). The heap never holds more than k
            entries at once.

        Time Complexity:  O(N log k) — N total nodes, each pushed/popped once;
                          heap operations cost O(log k).
        Space Complexity: O(k) — heap holds at most one node per list.
        """
        dummy = ListNode()
        tail = dummy
        heap: list[tuple[int, int, ListNode]] = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        counter = len(lists)   # unique tie-breaker for future pushes
        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next


# ── helpers ──────────────────────────────────────────────────────────────────

def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node: ListNode | None) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(sol.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test 2: All empty lists
    assert to_list(sol.mergeKLists([])) == []
    assert to_list(sol.mergeKLists([None])) == []

    # Test 3: Single list
    assert to_list(sol.mergeKLists([build_list([1, 2, 3])])) == [1, 2, 3]

    # Test 4: Lists with duplicate values across lists
    lists2 = [build_list([1, 1]), build_list([1, 1])]
    assert to_list(sol.mergeKLists(lists2)) == [1, 1, 1, 1]

    print("All test cases passed.")
