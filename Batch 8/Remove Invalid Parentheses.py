from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        LeetCode #301 - Remove Invalid Parentheses (Hard)

        Approach — backtracking with pre-counted minimum removals:
            First pass: count the minimum removals needed.
              • Scan left-to-right; track unmatched '(' with rm_open.
              • Each ')' that has a matching '(' reduces rm_open; otherwise
                it is an unmatched ')' and increments rm_close.
              • After the scan, rm_open unmatched '(' remain.

            Backtrack with parameters (i, open_cnt, rm_open, rm_close):
              • At each character, either include it or remove it (only
                parentheses may be removed; other characters must be kept).
              • Prune immediately if open_cnt < 0 (too many ')' so far) or
                rm_open < 0 or rm_close < 0 (over-removed).
              • A result string is valid when i == len(s) and all counters
                reach 0. Use a set to deduplicate.

        Time Complexity:  O(2^n · n) — up to 2^n paths; O(n) join per leaf.
                          Pruning reduces the practical search space greatly.
        Space Complexity: O(n) — recursion depth and path buffer.
        """
        # Count minimum removals needed
        rm_open = rm_close = 0
        for ch in s:
            if ch == "(":
                rm_open += 1
            elif ch == ")":
                if rm_open:
                    rm_open -= 1
                else:
                    rm_close += 1

        result: set[str] = set()

        def backtrack(
            i: int,
            path: List[str],
            open_cnt: int,
            rm_open: int,
            rm_close: int,
        ) -> None:
            if open_cnt < 0 or rm_open < 0 or rm_close < 0:
                return
            if i == len(s):
                if rm_open == 0 and rm_close == 0 and open_cnt == 0:
                    result.add("".join(path))
                return
            ch = s[i]
            # Option A: include the current character
            path.append(ch)
            if ch == "(":
                backtrack(i + 1, path, open_cnt + 1, rm_open, rm_close)
            elif ch == ")":
                backtrack(i + 1, path, open_cnt - 1, rm_open, rm_close)
            else:
                backtrack(i + 1, path, open_cnt, rm_open, rm_close)
            path.pop()
            # Option B: remove the current character (only parentheses)
            if ch == "(":
                backtrack(i + 1, path, open_cnt, rm_open - 1, rm_close)
            elif ch == ")":
                backtrack(i + 1, path, open_cnt, rm_open, rm_close - 1)

        backtrack(0, [], 0, rm_open, rm_close)
        return list(result)


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1
    result = sol.removeInvalidParentheses("()())()")
    assert sorted(result) == sorted(["(())()", "()()()"])

    # Test 2: LeetCode example 2 — string contains non-paren chars
    result = sol.removeInvalidParentheses("(a)())()")
    assert sorted(result) == sorted(["(a())()", "(a)()()"])

    # Test 3: Both parens must be removed — only empty string is valid
    result = sol.removeInvalidParentheses(")(")
    assert result == [""]

    # Test 4: Already valid — no removals needed
    result = sol.removeInvalidParentheses("()")
    assert result == ["()"]

    # Test 5: Empty string — trivially valid
    result = sol.removeInvalidParentheses("")
    assert result == [""]

    print("All test cases passed.")
