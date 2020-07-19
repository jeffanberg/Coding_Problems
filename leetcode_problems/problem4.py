'''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.'''


class Solution:    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        length = len(combined)
        if length % 2 != 0:
            median = combined[length // 2]
            return median
        else:
            median_ceiling = combined[-(length // -2)]
            median_floor = combined[(length // 2) - 1]
            return (median_floor + median_ceiling) / 2