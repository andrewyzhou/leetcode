class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        int cur = 1;
        vector<string> ans;
        ans.reserve(2 * target.back() - target.size());
        for (int x : target) {
            while (cur != x) {
                ans.push_back("Push");
                ans.push_back("Pop");
                cur++;
            }
            ans.push_back("Push");
            cur++;
        }
        return ans;
    }
};
