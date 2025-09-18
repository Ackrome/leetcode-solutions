import heapq
from collections import defaultdict

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.q = []
        self.d = defaultdict(list)
        for userId, taskId, priority in tasks:
            self.d[taskId] = [priority, userId]
            heapq.heappush(self.q, (-priority,  -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.d[taskId] = [priority, userId]
        heapq.heappush(self.q, (-priority,  -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.d[taskId][1]
        self.d[taskId] = (newPriority, userId)
        heapq.heappush(self.q, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.d[taskId]

    def execTop(self) -> int:
        while True:
            if not self.q:
                return -1

            mp, mt, userId = heapq.heappop(self.q)
            priority, taskId = -mp, -mt

            if self.d[taskId]:
                real_priority, real_userId = self.d[taskId]
                if (real_priority, real_userId) == (priority, userId):
                    del self.d[taskId]
                    return userId
                else:
                    heapq.heappush(self.q, (-real_priority, -taskId, real_userId))


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
