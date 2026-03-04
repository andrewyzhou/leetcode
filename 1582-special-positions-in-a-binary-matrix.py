class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        special_rows = [i for i in range(n) if sum(mat[i]) == 1]

        m = len(mat[0])
        special_cols = []
        for c in range(m):
            count = 0
            for r in range(n):
                count += mat[r][c]
            if count == 1:
                special_cols.append(c)
        
        ans = 0
        for r in special_rows:
            for c in special_cols:
                if mat[r][c] == 1:
                    ans += 1
        return ans