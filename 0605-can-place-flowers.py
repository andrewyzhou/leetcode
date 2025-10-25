class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        empty = 0
        if flowerbed[0] == 0:
            empty += 1
        for i in range(len(flowerbed)):                
            if flowerbed[i] or i == len(flowerbed) - 1:
                if i == len(flowerbed) - 1 and flowerbed[i] == 0:
                    empty += 2
                n -= max(0,(empty - 1) // 2 )
                empty = 0
                continue
            empty += 1
        return n <= 0
