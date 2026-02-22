from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        LeetCode #739 - Daily Temperatures (Medium)

        Approach:
            Monotonic decreasing stack of indices. Iterate left to right.
            Before pushing the current index, pop every index whose temperature
            is strictly less than the current temperature — those days have just
            found their "next warmer day". The wait for each popped index is
            simply (current index - popped index). Indices remaining in the
            stack at the end never found a warmer day, so they keep their
            default answer of 0.

        Time Complexity:  O(n) — each index is pushed and popped at most once.
        Space Complexity: O(n) — the stack and result array each hold at most
                          n entries.
        """
        n = len(temperatures)
        result = [0] * n
        stack: list[int] = []  # stores indices, decreasing by temperature

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    # Test 2: Monotonically decreasing — no warmer day ever
    assert sol.dailyTemperatures([90, 80, 70, 60]) == [0, 0, 0, 0]

    # Test 3: Monotonically increasing — each waits exactly 1 day
    assert sol.dailyTemperatures([60, 70, 80, 90]) == [1, 1, 1, 0]

    # Test 4: Single element
    assert sol.dailyTemperatures([50]) == [0]

    # Test 5: All equal — no warmer day
    assert sol.dailyTemperatures([70, 70, 70]) == [0, 0, 0]

    print("All test cases passed.")
