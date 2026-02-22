class Solution:
    def isValid(self, s: str) -> bool:
        """
        LeetCode #20 - Valid Parentheses (Easy)

        Approach:
            Use a stack. For every opening bracket push it. For every closing
            bracket check that the stack is non-empty and that the top of the
            stack is the matching opener; if not, return False immediately.
            After processing all characters the string is valid only when the
            stack is empty (no unmatched openers remain).

        Time Complexity:  O(n) — each character is pushed or popped at most once.
        Space Complexity: O(n) — in the worst case (all openers) the stack
                          holds n elements.
        """
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    sol = Solution()

    # Test 1: All matched pairs
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("{[()]}") is True

    # Test 2: Mismatched brackets
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False

    # Test 3: Unmatched opener
    assert sol.isValid("(") is False

    # Test 4: Unmatched closer
    assert sol.isValid(")") is False

    # Test 5: Empty string is valid
    assert sol.isValid("") is True

    print("All test cases passed.")
