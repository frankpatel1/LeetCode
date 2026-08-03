class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        const int MOD = 1e9 + 7;

        vector<vector<vector<int>>> dp(
            zero + 1,
            vector<vector<int>>(one + 1, vector<int>(2, 0))
        );

        for (int i = 1; i <= min(zero, limit); i++)
            dp[i][0][0] = 1;

        for (int j = 1; j <= min(one, limit); j++)
            dp[0][j][1] = 1;

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                int remove0 = (i - limit - 1 >= 0) ? dp[i - limit - 1][j][1] : 0;
                int remove1 = (j - limit - 1 >= 0) ? dp[i][j - limit - 1][0] : 0;

                dp[i][j][0] = ((long long)dp[i - 1][j][0] +
                               dp[i - 1][j][1] - remove0 + MOD) % MOD;

                dp[i][j][1] = ((long long)dp[i][j - 1][0] +
                               dp[i][j - 1][1] - remove1 + MOD) % MOD;
            }
        }

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD;
    }
};