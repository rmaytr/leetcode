from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        LeetCode #26 - Remove Duplicates from Sorted Array (Easy)

        Approach:
            Slow/fast two-pointer technique on a sorted array. `slow` marks
            the write position for the next unique value. `fast` scans ahead;
            whenever it finds a value different from nums[slow], the value is
            written to nums[slow + 1] and slow is advanced. Because the array
            is sorted, duplicates are always contiguous.

        Time Complexity:  O(n) — single pass with the fast pointer.
        Space Complexity: O(1) — in-place modification, no extra storage.
        """
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Some duplicates
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2]

    # Test 2: Multiple groups of duplicates
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4]

    # Test 3: No duplicates
    nums = [1, 2, 3]
    k = sol.removeDuplicates(nums)
    assert k == 3 and nums[:k] == [1, 2, 3]

    # Test 4: Single element
    nums = [7]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [7]

    print("All test cases passed.")
