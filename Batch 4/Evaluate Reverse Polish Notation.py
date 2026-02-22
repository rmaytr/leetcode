from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        LeetCode #150 - Evaluate Reverse Polish Notation (Medium)

        Approach:
            Use a stack. Push integers as encountered. When an operator is
            found, pop the top two operands (b then a, preserving order),
            apply the operation, and push the result. At the end the stack
            holds exactly one value — the answer.

            Integer division truncates toward zero (Python's // floors toward
            negative infinity, so int() is used for the division case to match
            C-style truncation required by the problem).

        Time Complexity:  O(n) — each token is processed exactly once.
        Space Complexity: O(n) — at most n//2 + 1 values on the stack.
        """
        stack: list[int] = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == "__main__":
    sol = Solution()

    # Test 1: (2 + 1) * 3 = 9
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9

    # Test 2: 4 + (13 / 5) = 6
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6

    # Test 3: Multi-operator expression
    assert sol.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ) == 22

    # Test 4: Single number
    assert sol.evalRPN(["42"]) == 42

    # Test 5: Truncation toward zero (-3 / 2 = -1, not -2)
    assert sol.evalRPN(["-3", "2", "/"]) == -1

    print("All test cases passed.")
