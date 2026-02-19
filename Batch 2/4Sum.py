from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        LeetCode #18 - 4Sum (Medium)

        Approach:
            Generalises 3Sum: sort the array, then use two nested loops for
            the first two anchors (i, j), and a two-pointer squeeze for the
            remaining pair. Duplicate skipping at each anchor level ensures
            the result set contains no repeated quadruplets without needing
            any additional data structure.

            Pruning:
              - If the four smallest remaining values exceed target → break.
              - If the four largest remaining values are below target → skip.
            These cuts can dramatically reduce iterations on large inputs.

        Time Complexity:  O(n³) — O(n log n) sort + O(n²) anchor pairs
                          each with an O(n) two-pointer inner scan.
        Space Complexity: O(1) extra (ignoring output list and sort buffer).
        """
        nums.sort()
        n = len(nums)
        result: List[List[int]] = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case from LeetCode
    result = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
    assert sorted(result) == sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    # Test 2: All zeros
    assert sol.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]

    # Test 3: No valid quadruplets
    assert sol.fourSum([1, 2, 3, 4], 100) == []

    # Test 4: Duplicates in input
    result = sol.fourSum([2, 2, 2, 2, 2], 8)
    assert result == [[2, 2, 2, 2]]

    print("All test cases passed.")
