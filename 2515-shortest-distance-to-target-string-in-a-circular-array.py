class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        return min(map(lambda t: min((startIndex - t + len(words)) % len(words), (t - startIndex + len(words)) % len(words)), [i for i, word in enumerate(words) if word == target]), default = -1)