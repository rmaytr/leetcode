class Solution:
    def climbStairs(self, n: int) -> int:
        """
        LeetCode #70 - Climbing Stairs (Easy)

        Approach — Fibonacci recurrence with O(1) rolling variables:
            The number of ways to reach step n equals the number of ways to
            reach step n-1 (then take 1 step) plus the number of ways to reach
            step n-2 (then take 2 steps). This is exactly the Fibonacci
            sequence: f(1)=1, f(2)=2, f(n)=f(n-1)+f(n-2).
            Two variables replace the full array, keeping space constant.

        Time Complexity:  O(n).
        Space Complexity: O(1).
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — 2 ways: {1+1, 2}
    assert sol.climbStairs(2) == 2

    # Test 2: LeetCode example 2 — 3 ways: {1+1+1, 1+2, 2+1}
    assert sol.climbStairs(3) == 3

    # Test 3: Base case
    assert sol.climbStairs(1) == 1

    # Test 4: Fibonacci spot-checks
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(10) == 89

    # Test 5: Larger value
    assert sol.climbStairs(44) == 1134903170

    print("All test cases passed.")
