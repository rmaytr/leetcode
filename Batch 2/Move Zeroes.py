from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        LeetCode #283 - Move Zeroes (Easy)

        Approach:
            Slow/fast two-pointer technique. `slow` is the write cursor for
            the next non-zero value. `fast` scans every element; when it finds
            a non-zero, it swaps with the position at `slow` and advances
            `slow`. Swapping (rather than overwriting then zero-filling at the
            end) means each element is moved at most once and zero-fills happen
            implicitly through the swaps.

        Time Complexity:  O(n) — single pass.
        Space Complexity: O(1) — in-place, no auxiliary storage.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case from LeetCode
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    # Test 2: All zeroes
    nums = [0, 0, 0]
    sol.moveZeroes(nums)
    assert nums == [0, 0, 0]

    # Test 3: No zeroes (array unchanged)
    nums = [1, 2, 3]
    sol.moveZeroes(nums)
    assert nums == [1, 2, 3]

    # Test 4: Zero at end only
    nums = [1, 2, 0]
    sol.moveZeroes(nums)
    assert nums == [1, 2, 0]

    print("All test cases passed.")
