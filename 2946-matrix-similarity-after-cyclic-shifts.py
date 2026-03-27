class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        for i in range(len(mat)):
            if i % 2 == 0:
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
            else:
                if mat[i] != mat[i][-k:] + mat[i][:-k]:
                    return False
        return True