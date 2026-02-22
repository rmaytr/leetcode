class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        LeetCode #143 - Reorder List (Medium)

        Approach:
            Three-phase in-place algorithm, all O(1) auxiliary space:
            1. Find the middle using slow/fast pointers; split the list in two.
            2. Reverse the second half in place.
            3. Merge the two halves by alternating nodes:
               L0 → Rn → L1 → Rn-1 → …

            Modifies the list in place; does not allocate new nodes.

        Time Complexity:  O(n) — three linear passes over (parts of) the list.
        Space Complexity: O(1) — no auxiliary data structures.
        """
        if not head or not head.next:
            return

        # Phase 1: find the middle (slow ends at the left-middle for even lengths)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Phase 2: reverse the second half
        second = slow.next
        slow.next = None       # cut the list
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev          # head of reversed second half

        # Phase 3: merge alternately
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


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

    # Test 1: Even-length list
    head = build_list([1, 2, 3, 4])
    sol.reorderList(head)
    assert to_list(head) == [1, 4, 2, 3]

    # Test 2: Odd-length list
    head = build_list([1, 2, 3, 4, 5])
    sol.reorderList(head)
    assert to_list(head) == [1, 5, 2, 4, 3]

    # Test 3: Single element — no change
    head = build_list([1])
    sol.reorderList(head)
    assert to_list(head) == [1]

    # Test 4: Two elements
    head = build_list([1, 2])
    sol.reorderList(head)
    assert to_list(head) == [1, 2]

    print("All test cases passed.")
