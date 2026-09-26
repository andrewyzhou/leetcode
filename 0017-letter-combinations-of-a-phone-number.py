w: dict[int, str] = {}

char = ord('a')
for num in range(2, 10):
    num_chars = 4 if num == 7 or num == 9 else 3
    w[num] = [chr(char + i) for i in range(num_chars)]
    char += num_chars

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 1:
            return w[int(digits[0])]
        return [x + rest for x in w[int(digits[0])] for rest in self.letterCombinations(digits[1:])]
