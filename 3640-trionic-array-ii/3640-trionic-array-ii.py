class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        result = float("-inf")
        left = p = q = 0
        prefix = nums[0]
        
        for right in range(1, len(nums)):
            prefix += nums[right]
            
            if nums[right - 1] > nums[right]:
                # We hit a peak point! (Flipped from increasing to decreasing)
                if right - 2 >= 0 and nums[right - 2] < nums[right - 1]:
                    p = right - 1
                
                # Prune negative elements from the left boundary to maximize the sum,
                # ensuring we don't cross q or break structural requirements.
                while left < q or (nums[left] < 0 and left + 1 < p):
                    prefix -= nums[left]
                    left += 1
                    
            elif nums[right - 1] < nums[right]:
                # We hit a valley point! (Flipped from decreasing to increasing)
                if right - 2 >= 0 and nums[right - 2] > nums[right - 1]:
                    q = right - 1
                
                # If left != p, it implies we have established a valid increasing-decreasing base
                if left != p:
                    result = max(result, prefix)
                    
            else:
                # Flat element values break strict monotonicity -> full reset
                left = p = q = right
                prefix = nums[right]
                
        return result