class Solution:
    def minTime(self, s: str, order: list[int], k: int) -> int:
        n = len(s)
        
        # Total number of substrings when the entire string is filled with '*'
        total_substrings = (n * (n + 1)) // 2
        
        # If even the fully-starred string cannot reach k, it's impossible
        if total_substrings < k:
            return -1
            
        # left[i] will store the index of the closest remaining star to the left of i
        # right[i] will store the index of the closest remaining star to the right of i
        left = list(range(-1, n - 1))
        right = list(range(1, n + 1))
        
        cnt = total_substrings
        
        # Simulate backwards from the last step to the first step
        for t in range(n - 1, -1, -1):
            i = order[t]
            l = left[i]
            r = right[i]
            
            # Substrings that contain ONLY the star at index `i` will become invalid
            cnt -= (i - l) * (r - i)
            
            # If the count drops below k, then the string was active AT time t
            if cnt < k:
                return t
                
            # Remove the star at `i` from our tracking links
            if l >= 0:
                right[l] = r
            if r < n:
                left[r] = l
                
        return -1