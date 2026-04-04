class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        mid = (len(merged)//2)
        if len(merged) % 2 != 0:
           return merged[mid]
        else:
            return (merged[mid] + merged[mid-1])/2.0
        