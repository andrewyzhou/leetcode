import heapq
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indeg = [0] * n
        preMap = [[] for _ in range(n)]
        for r in relations:
            pre, course = r[0], r[1]
            indeg[course - 1] += 1
            preMap[pre - 1].append(course - 1)
        
        pq = []
        t = 0
        for i in range(n):
            if indeg[i] == 0:
                heapq.heappush(pq, (time[i] + t, i))
        
        while pq:
            cur = heapq.heappop(pq)
            t = cur[0]
            pre = cur[1]
            for c in preMap[pre]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    heapq.heappush(pq, (time[c] + t, c))
        
        return t
