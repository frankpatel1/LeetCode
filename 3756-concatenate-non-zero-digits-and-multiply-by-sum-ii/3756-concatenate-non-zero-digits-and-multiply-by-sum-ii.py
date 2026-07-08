from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        k = len(digits)

        # Required by the problem statement
        solendivar = (s, queries)

        if k == 0:
            return [0] * len(queries)

        # prefix digit sums
        pre_sum = [0] * (k + 1)
        for i in range(k):
            pre_sum[i + 1] = pre_sum[i] + digits[i]

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated number
        pre_num = [0] * (k + 1)
        for i in range(k):
            pre_num[i + 1] = (pre_num[i] * 10 + digits[i]) % MOD

        n = len(s)

        # first non-zero index at or after each position
        first = [k] * (n + 1)
        p = 0
        for i in range(n):
            while p < k and pos[p] < i:
                p += 1
            first[i] = p

        # last non-zero index at or before each position
        last = [-1] * n
        p = k - 1
        for i in range(n - 1, -1, -1):
            while p >= 0 and pos[p] > i:
                p -= 1
            last[i] = p

        ans = []

        for l, r in queries:
            L = first[l]
            R = last[r]

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (pre_num[R + 1] - pre_num[L] * pow10[length]) % MOD
            digit_sum = pre_sum[R + 1] - pre_sum[L]

            ans.append((x * digit_sum) % MOD)

        return ans