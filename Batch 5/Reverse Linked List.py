class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        LeetCode #206 - Reverse Linked List (Easy)

        Approach:
            Iterative three-pointer technique. Maintain a prev pointer
            (initially None) and a curr pointer. On each step, save curr.next,
            flip curr.next to point backward at prev, then advance both prev
            and curr forward. When curr falls off the end, prev is the new head.

        Time Complexity:  O(n) — single pass through the list.
        Space Complexity: O(1) — only three pointer variables; no recursion stack.
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


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

    # Test 1: Standard case
    assert to_list(sol.reverseList(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

    # Test 2: Two elements
    assert to_list(sol.reverseList(build_list([1, 2]))) == [2, 1]

    # Test 3: Single element
    assert to_list(sol.reverseList(build_list([1]))) == [1]

    # Test 4: Empty list
    assert to_list(sol.reverseList(None)) == []

    print("All test cases passed.")
