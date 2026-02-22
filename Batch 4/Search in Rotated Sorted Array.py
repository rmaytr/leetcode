from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        LeetCode #33 - Search in Rotated Sorted Array (Medium)

        Approach:
            Modified binary search. At every midpoint one of the two halves
            [left, mid] or [mid, right] is guaranteed to be sorted. Identify
            which half is sorted by comparing nums[left] to nums[mid], then
            check whether the target falls within that sorted half. If it does,
            narrow the search to that half; otherwise search the other half.
            This gives a single-pass O(log n) solution with no need to first
            find the rotation pivot.

        Time Complexity:  O(log n) — search space halves each iteration.
        Space Complexity: O(1) — only scalar variables.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Left half [left, mid] is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half [mid, right] is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example — target in left sorted half
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    # Test 2: Target absent
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # Test 3: Single element, found
    assert sol.search([1], 1) == 0

    # Test 4: Single element, not found
    assert sol.search([1], 0) == -1

    # Test 5: No rotation
    assert sol.search([1, 2, 3, 4, 5], 3) == 2

    # Test 6: Target at the pivot boundary
    assert sol.search([6, 7, 1, 2, 3, 4, 5], 6) == 0

    print("All test cases passed.")
