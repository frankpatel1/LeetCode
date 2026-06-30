class Solution {
    public int minimumArrayLength(int[] nums) {
        int min = Integer.MAX_VALUE;

        // Find minimum element
        for (int num : nums) {
            min = Math.min(min, num);
        }

        int count = 0;

        for (int num : nums) {
            // If any number is not divisible by minimum,
            // answer is always 1.
            if (num % min != 0) {
                return 1;
            }

            if (num == min) {
                count++;
            }
        }

        return (count + 1) / 2;
    }
}