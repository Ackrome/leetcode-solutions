from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for p1, p2, p3 in combinations(points, r=3):
            res = max(res, 0.5 * abs((p1[0] - p2[0])*(p1[1] - p3[1]) - (p1[1] - p2[1])*(p1[0]-p3[0])))
        return res
