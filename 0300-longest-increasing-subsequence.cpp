class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        for (int x : nums) {
            auto i = lower_bound(tails.begin(), tails.end(), x);
            if (i == tails.end()) {
                tails.push_back(x);
            } else {
                *i = x;
            }
        }
        return tails.size();
    }
};
