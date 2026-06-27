class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        for mask in range(1 << n):
            subset = []

            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            ans.append(subset)

        return ans