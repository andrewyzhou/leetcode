class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        digits = 0
        while i < n:
            digits += 1
            i += digits * 9 * (10 ** (digits - 1))
        first = i - digits * 9 * (10 ** (digits - 1))
        numbers = (n - first + digits - 1) // digits
        place = (n - first - 1) % digits
        print("i:", i)
        print("first:", first)
        print("numbers:", numbers)
        print("place:", place)
        print(int(str(10 ** (digits - 1) - 1 + numbers)))
        return int(str(10 ** (digits - 1) - 1+ numbers)[place])