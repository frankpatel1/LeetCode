from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                nxt = cur * cur
                if nxt not in cnt:
                    break
                cur = nxt

            if cnt[cur] == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans