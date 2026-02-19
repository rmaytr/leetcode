from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        LeetCode #347 - Top K Frequent Elements (Medium)

        Approach:
            Bucket sort by frequency. Build a frequency map, then place each
            number into a bucket indexed by its frequency. Iterate the buckets
            from highest to lowest, collecting numbers until k elements are
            gathered. This beats the heap approach for large inputs because
            the bucket array has a fixed size of n+1.

        Time Complexity:  O(n) — frequency count + bucket fill + linear scan.
        Space Complexity: O(n) — frequency map and bucket array each size n.
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


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    # Test 2: k equals total unique elements
    assert sol.topKFrequent([1], 1) == [1]

    # Test 3: All same frequency
    result = sol.topKFrequent([1, 2], 2)
    assert sorted(result) == [1, 2]

    print("All test cases passed.")
