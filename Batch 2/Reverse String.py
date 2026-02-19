from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        LeetCode #344 - Reverse String (Easy)

        Approach:
            Classic two-pointer swap: left pointer starts at index 0, right
            pointer starts at the last index. Swap the characters and converge
            the pointers until they meet in the middle. Mutates in-place as
            required by the problem — no slice assignment or extra list.

        Time Complexity:  O(n) — n/2 swaps.
        Space Complexity: O(1) — in-place, only two index variables used.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Even-length input
    arr = ["h", "e", "l", "l", "o"]
    sol.reverseString(arr)
    assert arr == ["o", "l", "l", "e", "h"]

    # Test 2: Odd-length input (middle element stays put)
    arr = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(arr)
    assert arr == ["h", "a", "n", "n", "a", "H"]

    # Test 3: Single character
    arr = ["x"]
    sol.reverseString(arr)
    assert arr == ["x"]

    # Test 4: Two characters
    arr = ["a", "b"]
    sol.reverseString(arr)
    assert arr == ["b", "a"]

    print("All test cases passed.")
