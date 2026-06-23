class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:
            return m

        # length 2
        up = [0] * m
        down = [0] * m

        for x in range(m):
            up[x] = x              # previous value < current
            down[x] = m - 1 - x   # previous value > current

        for _ in range(3, n + 1):
            pref_up = [0] * (m + 1)
            pref_down = [0] * (m + 1)

            for i in range(m):
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD

            new_up = [0] * m
            new_down = [0] * m

            total_up = pref_up[m]
            total_down = pref_down[m]

            for x in range(m):
                # last move must have been DOWN,
                # previous value < current value x
                new_up[x] = pref_down[x]

                # last move must have been UP,
                # previous value > current value x
                new_down[x] = (total_up - pref_up[x + 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD