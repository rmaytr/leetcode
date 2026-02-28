from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode #46 - Permutations (Medium)

        Approach — backtracking with swap:
            At each DFS level `start`, swap nums[start] with every element
            nums[i] (i >= start), recurse for the remaining suffix, then swap
            back to restore the original order. When start reaches len(nums),
            the full array is one permutation — record a copy.

            This avoids an explicit `used` boolean array by treating the
            prefix nums[0..start-1] as "already chosen" and the suffix as
            "available" at each level.

        Time Complexity:  O(n! · n) — n! permutations, each copy is O(n).
        Space Complexity: O(n) — recursion depth; result list excluded.
        """
        result: List[List[int]] = []

        def backtrack(start: int) -> None:
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example — 3 elements, 6 permutations
    result = sol.permute([1, 2, 3])
    assert len(result) == 6
    assert sorted(result) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

    # Test 2: Two elements
    assert sorted(sol.permute([0, 1])) == sorted([[0, 1], [1, 0]])

    # Test 3: Single element — one permutation
    assert sol.permute([1]) == [[1]]

    # Test 4: Negative numbers
    result = sol.permute([-1, 0, 1])
    assert len(result) == 6

    print("All test cases passed.")
