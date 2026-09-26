from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        words = Counter(words)
        n = len(s)
        output = []
        for offset in range(word_len):
            l = offset
            found = defaultdict(int)
            for r in range(offset, n, word_len):
                new_word = s[r:r + word_len]
                if new_word not in words:
                    found.clear()
                    l = r + word_len
                    continue
                elif found[new_word] == words[new_word]:
                    while True:
                        leftWord = s[l:l + word_len]
                        found[leftWord] -= 1
                        l += word_len
                        if leftWord == new_word:
                            break
                found[new_word] += 1
                if found.items() == words.items():
                    output.append(l)
        return output
                    
