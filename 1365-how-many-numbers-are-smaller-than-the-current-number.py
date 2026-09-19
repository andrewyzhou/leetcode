class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        counts = [0] * 101
        for x in nums:
            counts[x] += 1
        less = [0] * 101
        for i in range(1, 101):
            less[i] = counts[i-1] + less[i-1]
        return [less[x] for x in nums]
        

