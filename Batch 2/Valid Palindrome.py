class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        LeetCode #125 - Valid Palindrome (Easy)

        Approach:
            Two-pointer scan on the original string, skipping non-alphanumeric
            characters in-place. Comparing with .lower() avoids allocating a
            cleaned copy of the string entirely.

        Time Complexity:  O(n) — each character is visited at most once.
        Space Complexity: O(1) — no auxiliary string is built.
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Classic palindrome with spaces and punctuation
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True

    # Test 2: Not a palindrome
    assert sol.isPalindrome("race a car") is False

    # Test 3: Empty / whitespace only (trivially palindrome)
    assert sol.isPalindrome(" ") is True

    # Test 4: Single character
    assert sol.isPalindrome("a") is True

    # Test 5: Mixed case
    assert sol.isPalindrome("Was it a car or a cat I saw?") is True

    print("All test cases passed.")
