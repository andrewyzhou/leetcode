class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        length = 2 ** n

        if k == length // 2:
            return "1"
        if k < length // 2:
            return self.findKthBit(n - 1, k)
        complement = self.findKthBit(n - 1, length - k)
        return "1" if complement == "0" else "0"