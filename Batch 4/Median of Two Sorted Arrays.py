from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        LeetCode #4 - Median of Two Sorted Arrays (Hard)

        Approach:
            Binary search on the smaller array. We look for the correct
            partition point in nums1 (call it i) such that the left halves of
            both arrays together contain exactly half of all elements. For each
            candidate i we derive j = half - i for nums2. The partition is
            valid when:
                nums1[i-1] <= nums2[j]  and  nums2[j-1] <= nums1[i]
            If not, adjust the binary search bounds. Use ±infinity sentinels
            for out-of-bounds accesses. Once the correct partition is found,
            the median follows directly from the four boundary values.

        Time Complexity:  O(log(min(m, n))) — binary search on the smaller array.
        Space Complexity: O(1) — only scalar variables.
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        left, right = 0, m

        while left <= right:
            i = left + (right - left) // 2  # partition in nums1
            j = half - i                    # partition in nums2

            nums1_left  = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i]     if i < m else float("inf")
            nums2_left  = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j]     if j < n else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Correct partition found
                if (m + n) % 2 == 1:
                    return float(min(nums1_right, nums2_right))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

        return 0.0  # unreachable for valid inputs


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example — odd total length
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0

    # Test 2: LeetCode example — even total length
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5

    # Test 3: One empty array
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    assert sol.findMedianSortedArrays([], [1, 2]) == 1.5

    # Test 4: Both single-element arrays
    assert sol.findMedianSortedArrays([3], [4]) == 3.5

    # Test 5: All elements of nums1 are smaller
    assert sol.findMedianSortedArrays([1, 2], [3, 4, 5]) == 3.0

    # Test 6: Duplicate values across arrays
    assert sol.findMedianSortedArrays([1, 1], [1, 1]) == 1.0

    print("All test cases passed.")
