class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(1,n):
            now = sorted([grid[j][j-i] for j in range(i)])
            for j in range(i):
                grid[j][j-i] = now[j]
                
        for i in range(n):
            now = sorted([grid[n-j-1][i-j] for j in range(i+1)])
            for j in range(i+1):
                grid[n-j-1][i-j] = now[j]
                
        return grid
