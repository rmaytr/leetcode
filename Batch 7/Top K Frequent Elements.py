from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        LeetCode #347 - Top K Frequent Elements (Medium)

        Approach — bucket sort for O(n):
            Count frequencies with Counter, then place each number into a
            bucket indexed by its frequency (bucket[freq] lists all numbers
            with that frequency). Scan buckets from highest frequency down,
            collecting elements until we have k results. The maximum possible
            frequency is n (when all elements are identical), so buckets has
            n+1 slots indexed 0..n.

            This beats the heap approach (O(n log k)) by avoiding heap ops.

        Time Complexity:  O(n) — counting + O(n) bucketing + O(n) linear scan.
        Space Complexity: O(n) — counter + bucket list.
        """
        count = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        result: List[int] = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


# ── tests ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test 1: LeetCode example 1
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    # Test 2: LeetCode example 2 — single element
    assert sol.topKFrequent([1], 1) == [1]

    # Test 3: k equals number of distinct elements
    assert sorted(sol.topKFrequent([1, 2, 3], 3)) == [1, 2, 3]

    # Test 4: All same element
    assert sol.topKFrequent([4, 4, 4, 4], 1) == [4]

    # Test 5: Multiple elements with same frequency — any k of them is valid
    result = sol.topKFrequent([1, 2, 3, 1, 2, 3], 2)
    assert len(result) == 2 and set(result).issubset({1, 2, 3})

    print("All test cases passed.")
