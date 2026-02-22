class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        LeetCode #19 - Remove Nth Node From End of List (Medium)

        Approach:
            Single-pass two-pointer technique with a dummy head. Move the fast
            pointer n+1 steps ahead of slow (both start at the dummy). Then
            advance both pointers together until fast reaches None. At that
            point slow is the node just before the target, so we can unlink
            the target with slow.next = slow.next.next. The dummy head absorbs
            the edge case where the head itself must be removed.

        Time Complexity:  O(L) — one traversal of the list (L = list length).
        Space Complexity: O(1) — only two pointer variables and a dummy node.
        """
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
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

    # Test 1: LeetCode example — remove 2nd from end
    assert to_list(sol.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]

    # Test 2: Remove the head (only node)
    assert to_list(sol.removeNthFromEnd(build_list([1]), 1)) == []

    # Test 3: Remove the head of a two-element list
    assert to_list(sol.removeNthFromEnd(build_list([1, 2]), 2)) == [2]

    # Test 4: Remove the last node
    assert to_list(sol.removeNthFromEnd(build_list([1, 2, 3]), 1)) == [1, 2]

    # Test 5: Remove the first node of a longer list
    assert to_list(sol.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 5)) == [2, 3, 4, 5]

    print("All test cases passed.")
