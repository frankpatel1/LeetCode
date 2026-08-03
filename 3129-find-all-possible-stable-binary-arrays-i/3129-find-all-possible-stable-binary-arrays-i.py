from functools import lru_cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(z, o, last):
            if z < 0 or o < 0:
                return 0
            if z == 0:
                return 1 if last == 1 and o <= limit else 0
            if o == 0:
                return 1 if last == 0 and z <= limit else 0

            if last == 0:
                return (
                    dfs(z - 1, o, 0)
                    + dfs(z - 1, o, 1)
                    - (dfs(z - limit - 1, o, 1) if z - limit - 1 >= 0 else 0)
                ) % MOD

            return (
                dfs(z, o - 1, 0)
                + dfs(z, o - 1, 1)
                - (dfs(z, o - limit - 1, 0) if o - limit - 1 >= 0 else 0)
            ) % MOD

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD