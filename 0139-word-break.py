class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for L in range(1, min(20, i) + 1):
                if dp[i - L] and s[i - L:i] in words:
                    dp[i] = True
                    break
        return dp[n]
