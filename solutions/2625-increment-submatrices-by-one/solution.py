class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        import numpy as np
        t = np.full((n,n),0)
        for i1,j1,i2,j2 in q: t[i1:i2+1,j1:j2+1] += 1
        return t.tolist()
