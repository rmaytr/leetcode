from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        LeetCode #643 - Maximum Average Subarray I (Easy)

        Approach:
            Fixed-size sliding window of width k. Compute the sum of the first
            window, then slide right by adding the incoming element and
            subtracting the outgoing element. Track the maximum window sum and
            convert to an average only once at the end to avoid repeated
            division.

        Time Complexity:  O(n) — each element enters and leaves the window once.
        Space Complexity: O(1) — only scalar accumulators.
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum / k


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75

    # Test 2: All same elements
    assert sol.findMaxAverage([5, 5, 5, 5], 2) == 5.0

    # Test 3: Window spans entire array
    assert abs(sol.findMaxAverage([3, 1, 4], 3) - 8 / 3) < 1e-5

    # Test 4: Negative numbers — max window is the least negative
    assert sol.findMaxAverage([-1, -2, -3, -4], 2) == -1.5

    print("All test cases passed.")
