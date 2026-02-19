from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        LeetCode #75 - Sort Colors (Medium)

        Approach:
            Dutch National Flag algorithm (Dijkstra). Three pointers:
              - low  : boundary of the '0' region (everything left is 0)
              - mid  : current element under inspection
              - high : boundary of the '2' region (everything right is 2)

            Invariant maintained at each step:
              nums[0..low-1]  == 0
              nums[low..mid-1] == 1
              nums[mid..high]  — unprocessed
              nums[high+1..n-1] == 2

            When nums[mid] == 0, swap with low and advance both low and mid.
            When nums[mid] == 2, swap with high and retreat high (don't
            advance mid because the swapped-in value is unprocessed).
            When nums[mid] == 1, just advance mid.

        Time Complexity:  O(n) — single pass; mid moves from 0 to high.
        Space Complexity: O(1) — in-place with three integer pointers.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard mixed input
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    # Test 2: Already sorted
    nums = [0, 1, 2]
    sol.sortColors(nums)
    assert nums == [0, 1, 2]

    # Test 3: All same color
    nums = [1, 1, 1]
    sol.sortColors(nums)
    assert nums == [1, 1, 1]

    # Test 4: Reverse sorted
    nums = [2, 1, 0]
    sol.sortColors(nums)
    assert nums == [0, 1, 2]

    print("All test cases passed.")
