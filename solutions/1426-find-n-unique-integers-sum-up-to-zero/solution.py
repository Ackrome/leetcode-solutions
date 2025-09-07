class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(n//2):
            result.extend([i+1,-(i+1)])
        if n%2!=0:
            result.append(0)

        return result
