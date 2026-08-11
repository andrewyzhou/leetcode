class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aIndices, bIndices = [], []
        for i in range(len(s)):
            if len(s) - i >= len(a) and s[i:i + len(a)] == a:
                aIndices.append(i)
            if len(s) - i >= len(b) and s[i:i + len(b)] == b:
                bIndices.append(i)
        ans = []
        b = 0
        for aIdx in aIndices:
            while b < len(bIndices) and bIndices[b] < aIdx - k:
                b += 1
            if b == len(bIndices):
                return ans
            if bIndices[b] <= aIdx + k:
                ans.append(aIdx)
        return ans
