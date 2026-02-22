from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        LeetCode #219 - Contains Duplicate II (Easy)

        Approach:
            Maintain a sliding window of at most k indices using a hash set.
            For each new element, check if it already exists in the set (meaning
            a duplicate within distance k). Then add the element and evict the
            element that is now more than k positions behind the current index
            to keep the window size bounded.

        Time Complexity:  O(n) — each element is added and removed from the
                          set at most once.
        Space Complexity: O(min(n, k)) — the window set holds at most k+1
                          elements.
        """
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Duplicate within range
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) is True

    # Test 2: Duplicate exists but too far apart
    assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) is True

    # Test 3: No duplicate
    assert sol.containsNearbyDuplicate([1, 2, 3, 4], 2) is False

    # Test 4: Indices exactly k apart
    assert sol.containsNearbyDuplicate([1, 2, 1], 2) is True

    # Test 5: Duplicate indices k+1 apart (just outside window)
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 2) is False

    print("All test cases passed.")
