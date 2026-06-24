class Solution {
public:
    static constexpr long long MOD = 1'000'000'007;

    using Matrix = vector<vector<long long>>;

    Matrix multiply(const Matrix& A, const Matrix& B) {
        int n = A.size();
        Matrix C(n, vector<long long>(n, 0));

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (!A[i][k]) continue;
                long long a = A[i][k];

                for (int j = 0; j < n; j++) {
                    if (!B[k][j]) continue;
                    C[i][j] = (C[i][j] + a * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    Matrix power(Matrix base, long long exp) {
        int n = base.size();
        Matrix res(n, vector<long long>(n, 0));

        for (int i = 0; i < n; i++) {
            res[i][i] = 1;
        }

        while (exp) {
            if (exp & 1) {
                res = multiply(res, base);
            }
            base = multiply(base, base);
            exp >>= 1;
        }

        return res;
    }

    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int sz = 2 * m;

        Matrix T(sz, vector<long long>(sz, 0));

        // State:
        // 0..m-1     -> last comparison was DOWN, next must go UP
        // m..2m-1    -> last comparison was UP, next must go DOWN

        for (int x = 0; x < m; x++) {
            // next must go UP
            for (int y = x + 1; y < m; y++) {
                T[x][m + y] = 1;
            }

            // next must go DOWN
            for (int y = 0; y < x; y++) {
                T[m + x][y] = 1;
            }
        }

        Matrix P = power(T, n - 2);

        vector<long long> init(sz, 0);

        // Length 2 initialization
        for (int a = 0; a < m; a++) {
            for (int b = 0; b < m; b++) {
                if (a == b) continue;

                if (a < b) {
                    init[m + b] = (init[m + b] + 1) % MOD;
                } else {
                    init[b] = (init[b] + 1) % MOD;
                }
            }
        }

        vector<long long> finalState(sz, 0);

        for (int i = 0; i < sz; i++) {
            if (!init[i]) continue;

            for (int j = 0; j < sz; j++) {
                finalState[j] =
                    (finalState[j] + init[i] * P[i][j]) % MOD;
            }
        }

        long long ans = 0;
        for (long long x : finalState) {
            ans = (ans + x) % MOD;
        }

        return (int)ans;
    }
};