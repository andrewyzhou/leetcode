class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        peak = height.index(max(height))
        ans = 0
        cur = height[left]
        while left != peak:
            cur = max(cur, height[left])
            ans += cur - height[left]
            left += 1
        cur = height[right]
        while right != peak:
            cur = max(cur, height[right])
            ans += cur - height[right]
            right -= 1
        return ans
