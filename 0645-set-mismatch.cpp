class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<char> seen(n + 1, 0);
        int ans = 0;
        for (int x : nums) {
            if(seen[x] == 1) {
                ans = x;
            }
            seen[x] = 1;
        }
        for (int i = 1; i <= n; ++i) {
            if(seen[i] == 0) {
                return {ans, i};
            }
        }
        return {};
    }
};
