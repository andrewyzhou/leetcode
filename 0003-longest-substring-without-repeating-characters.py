class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in window:
                while l < r:
                    leftChar = s[l]
                    window.remove(leftChar)
                    l += 1
                    if leftChar == s[r]:
                        break
            window.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
                    
                    

