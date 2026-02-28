from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        LeetCode #17 - Letter Combinations of a Phone Number (Medium)

        Approach — backtracking through digit-to-letter mapping:
            Map each digit 2–9 to its phone keypad letters. Backtrack depth-
            first: at index i, append each letter for digits[i], recurse for
            i+1, then pop. When the path length equals len(digits), join and
            record the combination. Return [] immediately for empty input.

        Time Complexity:  O(4^n · n) where n = len(digits) — at most 4 letters
                          per digit; each complete path costs O(n) to join.
        Space Complexity: O(n) — recursion depth and path buffer.
        """
        if not digits:
            return []

        phone: dict[str, str] = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        result: List[str] = []

        def backtrack(i: int, path: List[str]) -> None:
            if i == len(digits):
                result.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1 — digits "23"
    assert sorted(sol.letterCombinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )

    # Test 2: Empty input
    assert sol.letterCombinations("") == []

    # Test 3: Single digit
    assert sorted(sol.letterCombinations("2")) == ["a", "b", "c"]

    # Test 4: Digit with 4 letters
    assert sorted(sol.letterCombinations("7")) == ["p", "q", "r", "s"]

    # Test 5: Three digits — cardinality check
    result = sol.letterCombinations("234")
    assert len(result) == 3 * 3 * 3  # 3×3×3 = 27

    print("All test cases passed.")
