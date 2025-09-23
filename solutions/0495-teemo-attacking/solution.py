class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        restime = duration

        for i in range(len(timeSeries) - 1):
            if  timeSeries[i + 1] - timeSeries[i] > duration:
                restime += duration
            else:
                restime += timeSeries[i + 1] - timeSeries[i]
        return restime
            

