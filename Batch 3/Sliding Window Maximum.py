from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        LeetCode #239 - Sliding Window Maximum (Hard)

        Approach:
            Monotonic decreasing deque of indices. The deque always stores
            indices of elements that are candidates to be the window maximum —
            smaller elements that lie behind a larger one can never be the
            maximum of any future window, so they are discarded immediately.

            For each new element:
              1. Evict indices from the back that point to values <= nums[right]
                 (they are dominated and useless).
              2. Append the new index to the back.
              3. Evict the front index if it has slid out of the window
                 (index < right - k + 1).
              4. Once right >= k-1 the front of the deque is the window maximum.

        Time Complexity:  O(n) — each index is pushed and popped at most once.
        Space Complexity: O(k) — the deque holds at most k indices.
        """
        dq: deque[int] = deque()  # stores indices
        result: List[int] = []

        for right in range(len(nums)):
            # Remove indices of elements smaller than the current element
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)

            # Remove front index if it's outside the window
            if dq[0] < right - k + 1:
                dq.popleft()

            # Start recording once the first full window is formed
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Classic LeetCode example
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    # Test 2: Window equals array length
    assert sol.maxSlidingWindow([1, 3, 2], 3) == [3]

    # Test 3: Window of size 1 — returns the array itself
    assert sol.maxSlidingWindow([4, 2, 7, 1], 1) == [4, 2, 7, 1]

    # Test 4: Decreasing array
    assert sol.maxSlidingWindow([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]

    # Test 5: All equal elements
    assert sol.maxSlidingWindow([3, 3, 3, 3], 2) == [3, 3, 3]

    print("All test cases passed.")
