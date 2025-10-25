class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        def gcd(x,y):
            if (y == x):
                return x
            if (x < y):
                return gcd(x, y-x)
            return gcd(y, x)
        # if ay - bx = target ??? or bx - ay = target ???
        # 5 --> 3, 2 
        if target > (x + y):
            return False
        if target % gcd(x, y) == 0:
            return True
        
        return False
