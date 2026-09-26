from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lettersR = Counter(ransomNote)
        lettersM = Counter(magazine)
        for char, count in lettersR.items():
            if lettersM.get(char, 0) < count:
                return False
        return True