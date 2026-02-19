from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        LeetCode #1299 - Replace Elements with Greatest Element on Right Side (Easy)

        Approach:
            Scan the array right-to-left while tracking the running maximum
            of all elements seen so far (i.e., to the right of the current
            position). Replace each element in-place with that running max,
            then update the max. The last element always becomes -1.

        Time Complexity:  O(n) — single right-to-left pass.
        Space Complexity: O(1) — mutation is done in-place; no extra storage.
        """
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr


if __name__ == "__main__":
    sol = Solution()

    # Test 1: General case from LeetCode
    assert sol.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]

    # Test 2: Single element
    assert sol.replaceElements([400]) == [-1]

    # Test 3: Already decreasing
    assert sol.replaceElements([5, 4, 3, 2, 1]) == [4, 3, 2, 1, -1]

    print("All test cases passed.")
