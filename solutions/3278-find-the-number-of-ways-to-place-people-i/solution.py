class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Сортируем по x, а при равных x - по y в убывающем порядке
        points.sort(key=lambda p: (p[0], -p[1]))
        print(points)
        n = len(points)
        count = 0


        for i in range(n):
            for j in range(i+1,n):
                if points[i][1]<points[j][1]:
                    continue

                valid = True
                for k in range(i+1,j):
                    if points[j][1]<=points[k][1]<=points[i][1]:
                        valid = False
                        break
                
                if valid:
                    print( points[i], points[j])

                    count+=1
        return count
