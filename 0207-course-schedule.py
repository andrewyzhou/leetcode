class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            indeg[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        finish = 0
        while q:
            cur = q.popleft()
            finish += 1
            for nei in adj[cur]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return finish == numCourses
        