from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        LeetCode #39 - Combination Sum (Medium)

        Approach — backtracking with sorted early-exit:
            Sort candidates so we can break out of the loop the moment a
            candidate exceeds the remaining target. At each level, iterate
            from `start` onward — passing `i` (not `i+1`) to the next call
            allows unlimited reuse of the same element. When remaining hits
            exactly 0, record a copy of the current path.

        Time Complexity:  O(n^(T/m + 1)) where T = target, m = min candidate
                          — the recursion tree has depth at most T/m and
                          branches at most n ways at each level.
        Space Complexity: O(T/m) — maximum recursion depth.
        """
        candidates.sort()
        result: List[List[int]] = []

        def backtrack(start: int, path: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break  # sorted: all further candidates also too large
                path.append(c)
                backtrack(i, path, remaining - c)  # i allows reuse
                path.pop()

        backtrack(0, [], target)
        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1
    result = sol.combinationSum([2, 3, 6, 7], 7)
    assert sorted(result) == sorted([[2, 2, 3], [7]])

    # Test 2: LeetCode example 2
    result = sol.combinationSum([2, 3, 5], 8)
    assert sorted(result) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    # Test 3: No combination possible
    assert sol.combinationSum([2], 1) == []

    # Test 4: Single candidate, exact target
    assert sol.combinationSum([3], 9) == [[3, 3, 3]]

    # Test 5: Target is a candidate itself
    result = sol.combinationSum([1, 2], 3)
    assert sorted(result) == sorted([[1, 1, 1], [1, 2]])

    print("All test cases passed.")
