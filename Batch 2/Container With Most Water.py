from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        LeetCode #11 - Container With Most Water (Medium)

        Approach:
            Two-pointer squeeze from both ends. The area between pointers is
            min(height[left], height[right]) * (right - left). Moving the
            taller pointer inward can never increase area (width shrinks and
            the limiting height stays the same or decreases). Therefore we
            always move the shorter pointer, giving us the best possible shot
            at finding a taller boundary as width decreases.

        Time Complexity:  O(n) — pointers traverse the array at most once total.
        Space Complexity: O(1) — only two pointers and a running max.
        """
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case from LeetCode
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # Test 2: Two elements
    assert sol.maxArea([1, 1]) == 1

    # Test 3: Increasing heights
    assert sol.maxArea([1, 2, 3, 4, 5]) == 6

    # Test 4: Tall walls at the edges
    assert sol.maxArea([10, 1, 1, 1, 10]) == 40

    print("All test cases passed.")
