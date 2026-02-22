from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        LeetCode #84 - Largest Rectangle in Histogram (Hard)

        Approach:
            Monotonic increasing stack of (index, height) pairs. The key
            insight: a bar can extend leftward as far as there are bars at
            least as tall. When a bar shorter than the stack top is encountered,
            every taller bar on the stack is "closed" — its maximum rectangle
            ends here. Pop each such bar, compute its area using the current
            index as the right boundary, and note how far left its start
            extends (it can inherit the start index of the popped bar). After
            scanning all bars, flush remaining stack entries using the total
            length as the right boundary.

        Time Complexity:  O(n) — each bar is pushed and popped at most once.
        Space Complexity: O(n) — the stack holds at most n entries.
        """
        stack: list[tuple[int, int]] = []  # (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, bar_h = stack.pop()
                max_area = max(max_area, bar_h * (i - idx))
                start = idx          # current bar can extend back to here
            stack.append((start, h))

        # Flush remaining bars — all extend to the right end
        n = len(heights)
        for start, h in stack:
            max_area = max(max_area, h * (n - start))

        return max_area


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

    # Test 2: Uniform heights — entire array is the rectangle
    assert sol.largestRectangleArea([3, 3, 3, 3]) == 12

    # Test 3: Single bar
    assert sol.largestRectangleArea([5]) == 5

    # Test 4: Ascending heights
    assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9

    # Test 5: Descending heights
    assert sol.largestRectangleArea([5, 4, 3, 2, 1]) == 9

    # Test 6: Valley shape
    assert sol.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12

    print("All test cases passed.")
