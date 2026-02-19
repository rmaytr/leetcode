from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        LeetCode #128 - Longest Consecutive Sequence (Medium)

        Approach:
            Convert the input to a set for O(1) lookups. Iterate through the
            set: for each number that is the START of a sequence (i.e., n-1
            is not in the set), count how far the consecutive run extends.
            Skipping non-start numbers ensures each element is visited at most
            twice total, keeping the algorithm linear despite the nested loop.

        Time Complexity:  O(n) — each element is processed at most twice.
        Space Complexity: O(n) — set stores all n elements.
        """
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n - 1) not in num_set:          # n is the start of a sequence
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4  # [1,2,3,4]

    # Test 2: Longer consecutive run with gaps
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    # Test 3: Empty array
    assert sol.longestConsecutive([]) == 0

    # Test 4: Single element
    assert sol.longestConsecutive([42]) == 1

    # Test 5: All duplicates
    assert sol.longestConsecutive([1, 1, 1, 1]) == 1

    print("All test cases passed.")
