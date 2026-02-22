from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        LeetCode #704 - Binary Search (Easy)

        Approach:
            Classic iterative binary search. Maintain an inclusive [left, right]
            boundary. At each step compute the midpoint using left + (right -
            left) // 2 to avoid integer overflow. If the midpoint value equals
            the target return immediately; otherwise discard the half that
            cannot contain the target by moving left or right inward.

        Time Complexity:  O(log n) — the search space halves on every iteration.
        Space Complexity: O(1) — only three scalar variables.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Target present — returns correct index
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4

    # Test 2: Target absent
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Test 3: Single-element array, target found
    assert sol.search([5], 5) == 0

    # Test 4: Single-element array, target absent
    assert sol.search([5], 3) == -1

    # Test 5: Target is the first element
    assert sol.search([1, 3, 5, 7, 9], 1) == 0

    # Test 6: Target is the last element
    assert sol.search([1, 3, 5, 7, 9], 9) == 4

    print("All test cases passed.")
