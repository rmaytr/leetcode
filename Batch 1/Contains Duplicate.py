from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        LeetCode #217 - Contains Duplicate (Easy)

        Approach:
            Stream elements into a set. As soon as an element is already
            present in the set, a duplicate has been found — return True
            immediately without scanning the rest of the array.

        Time Complexity:  O(n) — at most one full pass in the worst case.
        Space Complexity: O(n) — set holds up to n distinct elements.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Contains duplicate
    assert sol.containsDuplicate([1, 2, 3, 1]) is True

    # Test 2: All unique
    assert sol.containsDuplicate([1, 2, 3, 4]) is False

    # Test 3: Multiple duplicates
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    # Test 4: Single element
    assert sol.containsDuplicate([1]) is False

    print("All test cases passed.")
