class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> count(101);
        for (int x : nums) {
            count[x]++;
        }
        vector<int> less(101);
        for (int i = 1; i < 101; ++i) {
            less[i] = less[i - 1] + count[i - 1];
        }
        for (int i = 0; i < nums.size(); ++i) {
            nums[i] = less[nums[i]];
        }
        return nums;
    }
};
