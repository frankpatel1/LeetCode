class Solution {
    public boolean canSortArray(int[] nums) {
        int n = nums.length;
        int prevMax = Integer.MIN_VALUE;
        int i = 0;

        while (i < n) {
            int bits = Integer.bitCount(nums[i]);
            int currMin = nums[i];
            int currMax = nums[i];

            while (i < n && Integer.bitCount(nums[i]) == bits) {
                currMin = Math.min(currMin, nums[i]);
                currMax = Math.max(currMax, nums[i]);
                i++;
            }

            if (prevMax > currMin) {
                return false;
            }

            prevMax = currMax;
        }

        return true;
    }
}