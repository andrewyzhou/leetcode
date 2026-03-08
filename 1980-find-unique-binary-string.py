class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        strings = []
        for i in range(1 << n):
            curr = format(i, f'0{n}b')
            if curr not in nums:
                return curr
