class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        now=0;out=0
        for i in target:
            if now<i:
                out+=i-now
            now=i
        return out
