class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore
        counter = 0
        candidate = None
        for i in nums:
            if counter == 0:
                candidate = i
                counter+=1
            elif candidate==i:
                counter+=1
            else:
                counter-=1
        return candidate

