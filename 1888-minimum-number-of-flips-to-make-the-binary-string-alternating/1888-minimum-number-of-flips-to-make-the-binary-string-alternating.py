class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        pattern = "01"

        # Mismatches with alternating pattern starting with '0'
        cnt = 0
        for i, ch in enumerate(s):
            if ch != pattern[i & 1]:
                cnt += 1

        ans = min(cnt, n - cnt)

        # Simulate all rotations
        for i in range(n):
            if s[i] != pattern[i & 1]:
                cnt -= 1
            if s[i] != pattern[(i + n) & 1]:
                cnt += 1
            ans = min(ans, cnt, n - cnt)

        return ans