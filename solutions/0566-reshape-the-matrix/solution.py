class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        flat = [col for row in mat for col in row]

        ans = []
        for i in range(r):
            ans.append(flat[i * c : (i + 1) * c])
        
        return ans
