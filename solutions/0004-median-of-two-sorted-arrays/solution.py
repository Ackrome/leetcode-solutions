class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = sorted(nums1+nums2)
        if len(k)%2==0:
            return (k[len(k)//2] + k[len(k)//2-1])/2
        return k[len(k)//2]
