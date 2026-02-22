class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """
        LeetCode #2 - Add Two Numbers (Medium)

        Approach:
            Simulate elementary addition digit-by-digit from least-significant
            to most-significant (the lists are already stored in reverse order).
            Use a dummy head and a carry variable. On each iteration, sum the
            current digits plus carry, produce a new node with (total % 10),
            and propagate carry = total // 10. Continue until both lists are
            exhausted and carry is zero.

        Time Complexity:  O(max(m, n)) — we iterate over both lists once;
                          at most one extra node for a final carry.
        Space Complexity: O(max(m, n)) — the result list has at most
                          max(m, n) + 1 nodes.
        """
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
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

    # Test 1: 342 + 465 = 807  (stored as [2,4,3] + [5,6,4])
    assert to_list(sol.addTwoNumbers(build_list([2, 4, 3]), build_list([5, 6, 4]))) == [7, 0, 8]

    # Test 2: 0 + 0
    assert to_list(sol.addTwoNumbers(build_list([0]), build_list([0]))) == [0]

    # Test 3: Carry propagation across many digits
    # 9999999 + 9999 = 10009998
    assert to_list(sol.addTwoNumbers(
        build_list([9, 9, 9, 9, 9, 9, 9]),
        build_list([9, 9, 9, 9])
    )) == [8, 9, 9, 9, 0, 0, 0, 1]

    # Test 4: Different lengths, carry at the end
    # 99 + 1 = 100
    assert to_list(sol.addTwoNumbers(build_list([9, 9]), build_list([1]))) == [0, 0, 1]

    print("All test cases passed.")
