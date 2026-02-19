from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        LeetCode #42 - Trapping Rain Water (Hard)

        Approach:
            Two-pointer technique with running left/right maximums.
            At any position the water trapped above it equals:
                min(max_left, max_right) - height[i]

            We don't need to know the exact max on both sides simultaneously.
            If max_left <= max_right, the water above the left pointer is
            determined solely by max_left (because max_right is at least as
            tall), so we can safely compute and accumulate it, then advance
            left. Symmetrically for the right side.

            This avoids the two preprocessing arrays (prefix max, suffix max)
            used in the O(n) space approach, cutting space to O(1).

        Time Complexity:  O(n) — single pass; each element visited at most once.
        Space Complexity: O(1) — four integer variables only.
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]

        return water


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case from LeetCode (answer = 6)
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    # Test 2: Second standard case (answer = 9)
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9

    # Test 3: No water trapped (monotonically increasing)
    assert sol.trap([1, 2, 3, 4, 5]) == 0

    # Test 4: No water trapped (monotonically decreasing)
    assert sol.trap([5, 4, 3, 2, 1]) == 0

    # Test 5: Single valley
    assert sol.trap([3, 0, 3]) == 3

    # Test 6: Empty input
    assert sol.trap([]) == 0

    print("All test cases passed.")
