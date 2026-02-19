from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        LeetCode #238 - Product of Array Except Self (Medium)

        Approach:
            Two-pass prefix/suffix product without using division.
            Pass 1 (left to right): result[i] holds the product of all
              elements strictly to the left of index i.
            Pass 2 (right to left): multiply each result[i] by the running
              suffix product (product of all elements strictly to the right).
            This achieves the output array in O(1) extra space (the output
            array itself is not counted per the problem constraints).

        Time Complexity:  O(n) — two linear passes.
        Space Complexity: O(1) extra — only the output array and a single
                          integer accumulator are used beyond the input.
        """
        n = len(nums)
        result = [1] * n

        # Forward pass: result[i] = product of nums[0..i-1]
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Backward pass: multiply by product of nums[i+1..n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    # Test 2: Contains zero
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    # Test 3: Two elements
    assert sol.productExceptSelf([2, 3]) == [3, 2]

    print("All test cases passed.")
