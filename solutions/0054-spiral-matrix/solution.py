class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        top = 0
        right = n - 1
        left = 0
        bottom = m - 1
        direction = 0
        res = []
        while top<=bottom and left <=right:
            if direction == 0:
                res.extend([matrix[top][i] for i in range(left, right+1)])
                top+=1
                direction = 1
            elif direction == 1:
                res.extend([matrix[i][right] for i in range(top,bottom +1)])
                right -=1
                direction = 2
            elif direction == 2:
                res.extend([matrix[bottom][i] for i in range(right, left-1, -1)])
                bottom-=1
                direction = 3
            else:
                res.extend([matrix[i][left] for i in range(bottom, top-1, -1)])
                left+=1
                direction = 0
        return res
