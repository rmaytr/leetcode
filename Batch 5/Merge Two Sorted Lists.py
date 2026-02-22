class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """
        LeetCode #21 - Merge Two Sorted Lists (Easy)

        Approach:
            Use a dummy head node to eliminate edge-case handling for an empty
            result list. Maintain a tail pointer and repeatedly attach the
            smaller of the two current heads, advancing that list's pointer.
            When one list is exhausted, splice the remainder of the other list
            directly — no need to copy nodes.

        Time Complexity:  O(m + n) — every node is visited exactly once.
        Space Complexity: O(1) — only the dummy head and tail pointer; no new
                          nodes are allocated.
        """
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
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
    assert to_list(sol.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]

    # Test 2: Both empty
    assert to_list(sol.mergeTwoLists(None, None)) == []

    # Test 3: One list empty
    assert to_list(sol.mergeTwoLists(None, build_list([0]))) == [0]

    # Test 4: Lists of different lengths
    assert to_list(sol.mergeTwoLists(build_list([1, 3, 5, 7]), build_list([2, 4]))) == [1, 2, 3, 4, 5, 7]

    # Test 5: All elements of list1 are smaller
    assert to_list(sol.mergeTwoLists(build_list([1, 2, 3]), build_list([4, 5, 6]))) == [1, 2, 3, 4, 5, 6]

    print("All test cases passed.")
