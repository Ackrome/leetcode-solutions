from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            window = nums[i:k+i]
            freq = Counter(window)
            sorted_freq = sorted(freq.items(), key = lambda a: (-a[1], -a[0]))
            top_x = set(num for num, _ in sorted_freq[:x])
            res.append(sum(num for num in window if num in top_x))
        
        return res
