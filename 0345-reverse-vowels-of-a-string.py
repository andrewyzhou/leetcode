class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        chars = ''
        for i in s:
            if i.lower() in vowels:
                chars = i + chars
        count = 0
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s = s[:i] + chars[count] + s[i+1:]
                count += 1
        return s
