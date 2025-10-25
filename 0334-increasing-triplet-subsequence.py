class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pre = [False] * len(nums) 
        post = [False] * len(nums) 
        mi = nums[0]
        for i in range(len(nums)):
            mi = min(mi, nums[i])
            if nums[i] > mi:
                pre[i] = True
        ma = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            ma = max(ma, nums[i])
            if nums[i] < ma:
                post[i] = True
        for i in range(len(nums)):
            if pre[i] and post[i]:
                return True
        return False

            
        
