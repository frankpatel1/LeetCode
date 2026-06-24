class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> ans = {0};

        for (int bit = 0; bit < n; bit++) {
            int add = 1 << bit;

            for (int i = ans.size() - 1; i >= 0; i--) {
                ans.push_back(ans[i] + add);
            }
        }

        return ans;
    }
};