class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        shorter = min([str1, str2], key=len)
        for i in range(len(shorter), 0, -1):
            if shorter[:i] * (len(str1) // i) == str1 and shorter[:i] * (len(str2) // i) == str2:
                return shorter[:i]
        return ""
        
