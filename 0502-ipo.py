class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(capital)
        indices = sorted(range(len(capital)), key=lambda i: capital[i])
        capital = [capital[i] for i in indices]
        profits = [profits[i] for i in indices]
        maxHeap = []
        bank = w
        projectIdx = 0
        for i in range(k):
            while projectIdx < n and bank >= capital[projectIdx]:
                heapq.heappush(maxHeap, -1 * profits[projectIdx])
                projectIdx += 1
            if not maxHeap:
                break
            bank += -1 * heapq.heappop(maxHeap)
        return bank
