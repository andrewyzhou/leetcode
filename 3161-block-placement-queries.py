from sortedcontainers import SortedList

class MaxSegTree:
    def __init__(self, length):
        self.n = 1
        while self.n < length:
            self.n *= 2
        self.tree = [0] * (2 * self.n)

    def set(self, i, value):
        i += self.n
        self.tree[i] = value

        while i > 1:
            i //= 2
            self.tree[i] = max(
                self.tree[2 * i],
                self.tree[2 * i + 1]
                )
    
    def query(self, x, sz):
        left = self.n
        right = self.n + x

        maxGap = 0
        while left <= right:
            if left % 2:
                maxGap = max(maxGap, self.tree[left])
                left += 1
            if right % 2 == 0:
                maxGap = max(maxGap, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        
        return maxGap >= sz

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxDist = max(queries, key=lambda x:x[1])[1]
        tree = MaxSegTree(maxDist + 2) # accomodates sentinel at idx = maxDist + 1
        obstacles = SortedList([0, maxDist + 1])

        output = []
        for q in queries:
            x = q[1]
            if q[0] == 1:
                obstacles.add(x)
                xIdx = obstacles.bisect_left(x)
                pred = obstacles[xIdx - 1]
                succ = obstacles[xIdx + 1]
                tree.set(x, x - pred)
                tree.set(succ, succ - x)
            else:
                sz = q[2]
                rightGap = x - obstacles[obstacles.bisect_left(x) - 1]
                output.append(tree.query(x, sz) or rightGap >= sz)
        return output

        