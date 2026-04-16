from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        positions = defaultdict(list)
        positions_positions = []
        for i, num in enumerate(nums):
            positions_positions.append(len(positions[num]))
            positions[num].append(i)
        ans = []
        n = len(nums)
        for q in queries:
            if len(positions[nums[q]]) == 1:
                ans.append(-1)
            else:
                matches = positions[nums[q]]
                middle = positions_positions[q]
                left = (middle - 1) % len(matches)
                right = (middle + 1) % len(matches)
                ans.append(min((q - matches[left] + n) % n, (matches[right] - q + n) % n))
        return ans