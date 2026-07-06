class Solution {
public:
    int minCut(string s) {

        int n = s.size();

        vector<vector<bool>> pal(n, vector<bool>(n, false));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {

                if (s[i] == s[j] &&
                    (j - i <= 2 || pal[i + 1][j - 1])) {

                    pal[i][j] = true;
                }
            }
        }

        vector<int> dp(n + 1, INT_MAX);

        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--) {

            for (int j = i; j < n; j++) {

                if (pal[i][j]) {

                    dp[i] = min(dp[i], 1 + dp[j + 1]);
                }
            }
        }

        return dp[0] - 1;
    }
};