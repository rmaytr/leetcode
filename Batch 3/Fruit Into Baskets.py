from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        LeetCode #904 - Fruit Into Baskets (Medium)

        Approach:
            "Two baskets" is equivalent to finding the longest contiguous
            subarray with at most 2 distinct values. Use a variable-size
            sliding window backed by a hash map that counts how many times
            each fruit type currently appears in the window. When the map
            grows to 3 distinct types, advance the left pointer until one
            type's count drops to zero and remove it. The window [left, right]
            always contains at most 2 distinct types.

        Time Complexity:  O(n) — each element enters and leaves the window at
                          most once.
        Space Complexity: O(1) — the basket map holds at most 3 entries before
                          shrinking back to 2.
        """
        basket: dict[int, int] = {}
        left = 0
        best = 0
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            window = right - left + 1
            if window > best:
                best = window
        return best


if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example
    assert sol.totalFruit([1, 2, 1]) == 3

    # Test 2: Three fruit types — must drop one
    assert sol.totalFruit([0, 1, 2, 2]) == 3

    # Test 3: Longer sequence
    assert sol.totalFruit([1, 2, 3, 2, 2]) == 4

    # Test 4: All same fruit
    assert sol.totalFruit([1, 1, 1, 1]) == 4

    # Test 5: Alternating three types
    assert sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5

    print("All test cases passed.")
