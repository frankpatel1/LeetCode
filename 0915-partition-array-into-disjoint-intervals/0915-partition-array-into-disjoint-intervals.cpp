class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int leftMax = nums[0];
        int currMax = nums[0];
        int pos = 0;

        for (int i = 1; i < nums.size(); i++) {
            currMax = max(currMax, nums[i]);

            if (nums[i] < leftMax) {
                leftMax = currMax;
                pos = i;
            }
        }

        return pos + 1;
    }
};