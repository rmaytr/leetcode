from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        LeetCode #287 - Find the Duplicate Number (Medium)

        Approach:
            Floyd's cycle detection — treat the array as an implicit linked
            list where index i points to node nums[i]. Because every value is
            in [1, n] and there is exactly one duplicate, two different indices
            point to the same node, which creates exactly one cycle. Index 0
            is the starting node (guaranteed no value points back to 0 since
            values are in [1, n]).

            Phase 1 — find any node inside the cycle:
                slow advances one step, fast advances two.
                They meet somewhere inside the cycle.

            Phase 2 — find the cycle entrance (= the duplicate):
                Reset one pointer to the start (index 0). Advance both one
                step at a time; they meet at the cycle entrance, which is the
                duplicate value.

        Time Complexity:  O(n) — both phases are linear.
        Space Complexity: O(1) — only two pointer variables; array unmodified.
        """
        # Phase 1: detect meeting point inside the cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find cycle entrance
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2

    # Test 2: Duplicate at the start of the cycle
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3

    # Test 3: Duplicate value is 1
    assert sol.findDuplicate([1, 1]) == 1

    # Test 4: Duplicate appears many times
    assert sol.findDuplicate([2, 2, 2, 2, 2]) == 2

    # Test 5: Larger array
    assert sol.findDuplicate([1, 2, 3, 4, 5, 3]) == 3

    print("All test cases passed.")
