import heapq
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        
        rain_days = defaultdict(list)
        for i, lake in enumerate(rains):
            if lake > 0:
                rain_days[lake].append(i)
        
        full_lakes = set()          
        pq = []                     
        result = [1] * len(rains)   
        for i in range(len(rains)):
            if rains[i] > 0:
                lake = rains[i]
                if lake in full_lakes:
                    return []
                full_lakes.add(lake)
                
                idx = next((j for j, day in enumerate(rain_days[lake]) if day == i), -1)
                if idx + 1 < len(rain_days[lake]):
                    next_rain = rain_days[lake][idx + 1]
                    heapq.heappush(pq, (next_rain, lake))
                
                result[i] = -1
            else:
                if pq:
                    _, lake = heapq.heappop(pq)
                    result[i] = lake
                    full_lakes.remove(lake)
        return result
