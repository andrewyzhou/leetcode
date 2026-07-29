class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            indeg[course] += 1
        
        ans = []
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                ans.append(i)

        finish = 0
        while q:
            cur = q.popleft()
            finish += 1
            for nei in adj[cur]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
                    ans.append(nei)
        if finish == numCourses:
            return ans
        return []
        