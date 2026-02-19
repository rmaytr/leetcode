from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        LeetCode #1 - Two Sum (Easy)

        Approach:
            Use a hash map to store each number and its index as we iterate.
            For each number, check if its complement (target - num) already
            exists in the map. If so, return the two indices immediately.

        Time Complexity:  O(n) — single pass through the array.
        Space Complexity: O(n) — hash map stores up to n elements.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

    # Test 2: Numbers not at the start
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]

    # Test 3: Duplicate values
    assert sol.twoSum([3, 3], 6) == [0, 1]

    print("All test cases passed.")
