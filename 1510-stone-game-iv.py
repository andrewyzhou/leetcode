import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # isLosing[k] = True if player with k stones left on their turn is lost
        # base case: k = 0 means the player already lost
        # recursive case: for all k > 0, if we can reach an isLosing state --> isLosing[k] = False
        # time complexity: O(n^1.5), n * sqrt(n) checks
        # memory complexity: O(n) for isLosing array
        isLosing = [True] * (n + 1)
        for cur in range(1, n + 1):
            for k in range(1, math.isqrt(cur) + 1):
                if isLosing[cur - k * k]:
                    isLosing[cur] = False
                    break
        return not isLosing[n]

if __name__ == "__main__":
    tests = [
        # (input n, expected output)
        (1, True),
        (2, False),
        (4, True),
        (7, False),
    ]

    sol = Solution()
    for n, expected in tests:
        result = sol.winnerSquareGame(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}  n={n}  expected={expected}  got={result}")
