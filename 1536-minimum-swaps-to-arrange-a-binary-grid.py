class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        right_one = [-1] * n

        for r in range(n):
            for i in range(n):
                if grid[r][i]:
                    right_one[r] = i
        
        sorted_ones = sorted(right_one)
        for i in range(n):
            if sorted_ones[i] > i:
                return -1

        swaps = 0
        for i in range(n):
            j = i
            while right_one[j] > i:
                j += 1

            swaps += j - i
            v = right_one.pop(j)
            right_one.insert(i, v)
        return swaps