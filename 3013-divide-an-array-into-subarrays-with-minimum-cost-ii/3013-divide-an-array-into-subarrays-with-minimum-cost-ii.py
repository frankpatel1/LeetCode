from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        if k == 1:
            return nums[0]

        small = SortedList()
        large = SortedList()
        small_sum = 0

        def add(x):
            nonlocal small_sum

            if len(small) < k - 1:
                small.add(x)
                small_sum += x
            elif x < small[-1]:
                y = small.pop()
                small_sum -= y
                large.add(y)
                small.add(x)
                small_sum += x
            else:
                large.add(x)

        def remove(x):
            nonlocal small_sum

            if x in small:
                small.remove(x)
                small_sum -= x
                if large:
                    y = large.pop(0)
                    small.add(y)
                    small_sum += y
            else:
                large.remove(x)

        for i in range(1, min(len(nums), dist + 2)):
            add(nums[i])

        ans = nums[0] + small_sum

        for i in range(dist + 2, len(nums)):
            remove(nums[i - dist - 1])
            add(nums[i])
            ans = min(ans, nums[0] + small_sum)

        return ans