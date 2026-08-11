class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        target = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                target += nums[i]
            else:
                break
        nums = set(nums)
        while target in nums:
            target += 1
        return target