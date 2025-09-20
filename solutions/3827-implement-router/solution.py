from collections import defaultdict, deque

class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.dest= defaultdict(deque)
        self.ht = set()
        self.ml = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        t = (timestamp,source,destination)
        if self.q:
            if t in self.ht:
                return False 
        if len(self.q) +1 > self.ml:
            self.forwardPacket()
        self.q.append(t)
        self.dest[destination].append(timestamp)
        self.ht.add(t)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        timestamp,source,destination = self.q.popleft()
        self.dest[destination].popleft()
        self.ht.remove((timestamp,source,destination))
        return [source, destination, timestamp]
        
        

    def bs_right (self,mx,x):
        low,high = -1,len(mx)
        while high-low>1:
            mid = low + (high-low)//2
            if mx[mid]<x:
                low=mid
            else:
                high=mid
        return high

    def bs_left (self,mx,x):
        low,high = -1,len(mx)
        while high-low>1:
            mid = low + (high-low)//2
            if mx[mid]>x:
                high=mid
            else:
                low=mid
        return high

    def getCount(self, destination, startTime, endTime):
        d = self.dest[destination]
        if not d:
            return 0
        a,b = self.bs_left(d,endTime) , self.bs_right(d,startTime)

        return a-b
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
