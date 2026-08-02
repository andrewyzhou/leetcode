class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0;
        int ans = nums.size() + 1;
        int win = 0;
        while (r < nums.size()) {
            while (win < target) {
                win += nums[r];
                r++;
                if (r == nums.size()) {
                    break;
                }
            }
            while (l < r) {
                if (win < target) {
                    break;
                }
                win -= nums[l];
                l++;
            }
            ans = min(ans, r - l + 1);
        }
        return (ans == nums.size() + 1) ? 0 : ans;
    }
};
