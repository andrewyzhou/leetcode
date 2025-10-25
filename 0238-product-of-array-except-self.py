class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = list(nums)
        suffix = list(nums)
        n = len(nums)
        if n <= 1:
            return list(nums)
        for i in range(1, n):
            prefix[i] *= prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] *= suffix[i + 1]
        
        res = list(nums)
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1, n - 1):
            res[i] = prefix[i - 1] * suffix[i + 1]
        return res
