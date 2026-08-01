class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix)-1
        c = 0
        while l <= h:
            m = (l+h)//2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] < target:
                l = m+1
                c = m
            else:
                h = m-1
                c = m-1
        
        l, h = 0, len(matrix[0])-1
        while l <= h:
            m = (l+h)//2
            if matrix[c][m] == target:
                return True
            if matrix[c][m] < target:
                l = m+1
            else: 
                h = m-1
        return False
