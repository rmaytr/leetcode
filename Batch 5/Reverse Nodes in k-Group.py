class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        LeetCode #25 - Reverse Nodes in k-Group (Hard)

        Approach:
            Iterative in-place reversal. Before reversing each group, count k
            nodes ahead to confirm a full group exists; if not, leave the
            remainder as-is. Reverse exactly k nodes using the standard
            three-pointer technique, then connect:
              - the previous group's tail  → new group head (returned by reverse)
              - the new group's tail (old head) → the next group's start
            A dummy head node simplifies connecting the very first group.

        Time Complexity:  O(n) — each node is reversed at most once.
        Space Complexity: O(1) — no recursion; only pointer variables.
        """
        dummy = ListNode(0, head)
        prev_tail = dummy

        while True:
            # Check if k nodes remain
            check = prev_tail
            for _ in range(k):
                check = check.next
                if not check:
                    return dummy.next  # fewer than k nodes left — done

            # Reverse k nodes starting from prev_tail.next
            group_head = prev_tail.next
            prev, curr = None, group_head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # prev  = new head of reversed group
            # curr  = first node of the next group
            # group_head = new tail of reversed group

            prev_tail.next = prev          # connect previous tail to new head
            group_head.next = curr         # connect new tail to rest of list
            prev_tail = group_head         # advance prev_tail for next iteration


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

    # Test 1: k=2, even split
    assert to_list(sol.reverseKGroup(build_list([1, 2, 3, 4]), 2)) == [2, 1, 4, 3]

    # Test 2: k=3, tail (fewer than k nodes) left as-is
    assert to_list(sol.reverseKGroup(build_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]

    # Test 3: k=1 — no change
    assert to_list(sol.reverseKGroup(build_list([1, 2, 3]), 1)) == [1, 2, 3]

    # Test 4: k equals list length — full reversal
    assert to_list(sol.reverseKGroup(build_list([1, 2, 3, 4]), 4)) == [4, 3, 2, 1]

    # Test 5: Single node
    assert to_list(sol.reverseKGroup(build_list([1]), 1)) == [1]

    print("All test cases passed.")
