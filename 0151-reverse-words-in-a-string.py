class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        prev = 0
        for i in range(len(s) + 1):
            if i == len(s) or (i > 0 and s[i-1] != ' ' and s[i] == ' ') or (i > 0 and s[i-1] == ' ' and s[i] != ' '):
                if s[i-1] != ' ':
                    words.append(s[prev:i])
                prev = i
        return ' '.join(words[::-1])
