class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        for elem in nums1:
            merged.append(elem)
        for elem in nums2:
            merged.append(elem)
        merged.sort()
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
