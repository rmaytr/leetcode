from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        LeetCode #167 - Two Sum II - Input Array Is Sorted (Medium)

        Approach:
            Exploit the sorted order with a two-pointer squeeze. Start with
            left at index 0 and right at the last index. If the sum equals
            the target, return the 1-indexed positions. If the sum is too
            small, advance left to increase it; if too large, retreat right
            to decrease it. The problem guarantees exactly one solution.

        Time Complexity:  O(n) — pointers traverse the array at most once.
        Space Complexity: O(1) — only two index variables used.
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1
        return []  # guaranteed to find a solution per problem constraints


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]

    # Test 2: Numbers in the middle
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]

    # Test 3: Negative numbers
    assert sol.twoSum([-1, 0], -1) == [1, 2]

    # Test 4: Larger array
    assert sol.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19) == [9, 10]

    print("All test cases passed.")
