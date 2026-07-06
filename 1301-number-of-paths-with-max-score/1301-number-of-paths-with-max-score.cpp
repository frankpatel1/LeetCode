class Solution {
public:
    const int MOD = 1e9 + 7;

    vector<int> pathsWithMaxScore(vector<string>& board) {

        int n = board.size();

        vector<vector<int>> score(n, vector<int>(n, -1));
        vector<vector<int>> ways(n, vector<int>(n, 0));

        score[n - 1][n - 1] = 0;
        ways[n - 1][n - 1] = 1;

        for (int i = n - 1; i >= 0; i--) {

            for (int j = n - 1; j >= 0; j--) {

                if (board[i][j] == 'X')
                    continue;

                if (i == n - 1 && j == n - 1)
                    continue;

                int best = -1;

                vector<pair<int,int>> prev = {
                    {i + 1, j},
                    {i, j + 1},
                    {i + 1, j + 1}
                };

                for (auto [x, y] : prev) {
                    if (x >= n || y >= n)
                        continue;

                    if (score[x][y] == -1)
                        continue;

                    best = max(best, score[x][y]);
                }

                if (best == -1)
                    continue;

                long long cnt = 0;

                for (auto [x, y] : prev) {
                    if (x >= n || y >= n)
                        continue;

                    if (score[x][y] == best) {
                        cnt = (cnt + ways[x][y]) % MOD;
                    }
                }

                int val = 0;

                if (isdigit(board[i][j]))
                    val = board[i][j] - '0';

                score[i][j] = best + val;
                ways[i][j] = cnt;
            }
        }

        if (ways[0][0] == 0)
            return {0, 0};

        return {score[0][0], ways[0][0]};
    }
};