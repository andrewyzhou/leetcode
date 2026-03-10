class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        @cache
        def f(q, p):
            if q < 1:
                return p < 1
            total = 0
            for k in range(min(l, q)):
                total += f(p, q - k - 1)
            return total

        return (f(z, o) + f(o, z)) % (10**9 + 7)
