from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode #15 - 3Sum (Medium)

        Approach:
            Sort the array, then for each element nums[i] (the anchor), run a
            two-pointer squeeze on the subarray to its right to find pairs
            that sum to -nums[i]. Duplicates are skipped at both the anchor
            and the inner pointer levels so the result set is automatically
            deduplicated without needing a set of tuples.

            Early termination: if nums[i] > 0, all remaining elements are
            non-negative, so no valid triplet can exist.

        Time Complexity:  O(n²) — O(n log n) sort + O(n) inner scan per anchor.
        Space Complexity: O(1) extra (ignoring the output list and sort buffer).
        """
        nums.sort()
        result: List[List[int]] = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate anchors
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    result = sol.threeSum([-1, 0, 1, 2, -1, -4])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]])

    # Test 2: No valid triplets
    assert sol.threeSum([0, 1, 1]) == []

    # Test 3: All zeros
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]

    # Test 4: Single valid triplet with duplicates in input
    result = sol.threeSum([-2, 0, 0, 2, 2])
    assert result == [[-2, 0, 2]]

    print("All test cases passed.")
