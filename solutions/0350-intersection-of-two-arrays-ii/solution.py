from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        res = []
        for x in d1:
            if x in d2:
                res.extend([x]*min(d1[x], d2[x]))

        return res
