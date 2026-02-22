class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        LeetCode #121 - Best Time to Buy and Sell Stock (Easy)

        Approach:
            Sliding window with a tracked minimum. Maintain the lowest price
            seen so far (the implicit left pointer of the window). For each
            price, compute the profit if sold today and update the best profit.
            Moving the minimum forward whenever a new low is found is equivalent
            to sliding the buy-day pointer — we never need to look back past
            the current minimum.

        Time Complexity:  O(n) — single pass through prices.
        Space Complexity: O(1) — only two scalar variables.
        """
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard LeetCode example
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    # Test 2: Prices only decrease — no profit possible
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

    # Test 3: Single element
    assert sol.maxProfit([5]) == 0

    # Test 4: Buy at start, sell at end
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

    # Test 5: Best window is not the global min/max pair
    assert sol.maxProfit([3, 1, 4, 8, 2, 9]) == 8

    print("All test cases passed.")
