class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        transformations = defaultdict(int)
        img1coords = []
        img2coords = []
        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    img1coords.append((r, c))
                if img2[r][c]:
                    img2coords.append((r, c))
        for x1, y1 in img1coords:
            for x2, y2 in img2coords:
                transformations[(x2 - x1, y2 - y1)] += 1
        if transformations:
            return max(transformations.values())
        return 0