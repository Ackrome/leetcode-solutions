class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals  = sorted(intervals, key = lambda x: x[0])
        c = 0
        for i in range(len(intervals)-1):
            if intervals[i-c][1]>=intervals[i+1-c][0]:
                intervals[i-c] = [intervals[i-c][0], max(intervals[i+1-c][1],intervals[i-c][1])]
                del intervals[i+1-c]
                c+=1
        return intervals
