class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        n = len(nums)
        if n == 1:
            return 0
        firstidx = float('inf')
        lastidx = -float('inf')
        for i in range(n):
            if s[i] != nums[i]:
                if i < firstidx:
                    firstidx = i
                if i > lastidx:
                    lastidx = i
        if lastidx == -float('inf'):
            return 0
        return lastidx - firstidx + 1
